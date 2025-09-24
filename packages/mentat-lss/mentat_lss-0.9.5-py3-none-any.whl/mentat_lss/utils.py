import yaml, os
from scipy.stats import qmc, norm
from torch.nn import functional as F
import numpy as np
import itertools
import torch


def load_config_file(config_file:str):
    """loads in the emulator config file as a dictionary object
    
    Args:
        config_file: Config file path and name to laod
    Raises:
        IOError: If config_file could not be read in
    """
    with open(config_file, "r") as file:
        try:
            config_dict = yaml.load(file, Loader=yaml.FullLoader)
        except:
            raise IOError(f"Could not load config yaml file at {config_file}")
    
    return config_dict


def get_parameter_ranges(cosmo_dict:dict):
    """Returns cosmology and bias parameter priors based on the input cosmo_dict
    
    Args:
        cosmo_dict (dict): dictionary of cosmology + nuisance parameter values and ranges
    Returns:
        params (list): name of parameters that are varied in the input cosmo_dict
        priors (np.array): min and max bounds of parameters varied in cosmo_dict. Has shape [len(param_names), 2]  
    """

    cosmo_params = {}
    for param in cosmo_dict["cosmo_params"]:
        if "prior" in cosmo_dict["cosmo_params"][param]:
            if "min" in cosmo_dict["cosmo_params"][param]["prior"]:
                cosmo_params[param] = [cosmo_dict["cosmo_params"][param]["prior"]["min"],
                                       cosmo_dict["cosmo_params"][param]["prior"]["max"]]
            else:
                cosmo_params[param] = [cosmo_dict["cosmo_params"][param]["prior"]["mean"] - 5*cosmo_dict["cosmo_params"][param]["prior"]["variance"],
                                       cosmo_dict["cosmo_params"][param]["prior"]["mean"] + 5*cosmo_dict["cosmo_params"][param]["prior"]["variance"]]

    nuisance_params = {}
    for param in cosmo_dict["nuisance_params"]:
        if "prior" in cosmo_dict["nuisance_params"][param]:
            if "min" in cosmo_dict["nuisance_params"][param]["prior"]:
                nuisance_params[param] = [cosmo_dict["nuisance_params"][param]["prior"]["min"],
                                          cosmo_dict["nuisance_params"][param]["prior"]["max"]]
            else:
                nuisance_params[param] = [cosmo_dict["nuisance_params"][param]["prior"]["mean"] - 5*cosmo_dict["nuisance_params"][param]["prior"]["variance"],
                                          cosmo_dict["nuisance_params"][param]["prior"]["mean"] + 5*cosmo_dict["nuisance_params"][param]["prior"]["variance"]]
    params_dict = {**cosmo_params, **nuisance_params}
    priors = np.array(list(params_dict.values()))
    params = list(params_dict.keys())
    return params, priors


def get_gaussan_priors(cosmo_dict:dict):
    """interprets the input cosmo_dict and outputs a list of scipy.stats.norm objects for use by Nautilus 

    Args:
        cosmo_dict (dict): dictionary of cosmology + nuisance parameter values and ranges

    Returns:
        priors (list): list of scipy.stats.norm objects corresponding to the Gaussian priors of prior_names
        prior_names (list): names of the corresponding priors in priors
    """
    priors, prior_names = [], []
    for param in cosmo_dict["cosmo_params"]:
        if "prior" in cosmo_dict["cosmo_params"][param]:
            if "mean" in cosmo_dict["cosmo_params"][param]["prior"]:
                priors.append(norm(cosmo_dict["cosmo_params"][param]["prior"]["mean"], cosmo_dict["cosmo_params"][param]["prior"]["variance"]))
                prior_names.append(param)

    for param in cosmo_dict["nuisance_params"]:
        if "prior" in cosmo_dict["nuisance_params"][param]:
            if "mean" in cosmo_dict["nuisance_params"][param]["prior"]:
                priors.append(norm(cosmo_dict["nuisance_params"][param]["prior"]["mean"], cosmo_dict["nuisance_params"][param]["prior"]["variance"]))
                prior_names.append(param)

    return priors, prior_names


def prepare_ps_inputs(sample:dict, cosmo_dict:dict, num_tracers:int, num_zbins:int):
    """takes a set of parameters and oragnizes them to the format expected by ps_theory_calculator
    
    Args:
        sample (dict): dictionary of (param_name, param_value)
        cosmo_dict (dict) dictionary of cosmology + nuisance parameter values and ranges
        num_tracers (int): number of correlated tracers to calculate
        num_zbins (int): number of independent redshift bins to calculate
    Returns:
        param_vector (np.array): 1D list of parameters that can be directly passed to ps_theory_calculator
    """
    param_vector = []
    # fill in cosmo params in the order ps_1loop expects
    for pname in list(cosmo_dict["cosmo_param_names"]):
        if pname in sample:
            #print(params.index(pname))
            param_vector.append(sample[pname])
        else:
            param_vector.append(cosmo_dict["cosmo_params"][pname]["value"])

    # fill in bias params
    for isample in range(num_tracers):
        for iz in range(num_zbins):
            sub_vector = []
            for pname in list(cosmo_dict["bias_param_names"] + 
                              cosmo_dict["counterterm_param_names"] + 
                              cosmo_dict["stochastic_param_names"]):
                key = pname+"_"+str(isample)+"_"+str(iz)

                if key in sample:
                    sub_vector.append(sample[key])
                elif pname in sample:
                    sub_vector.append(sample[pname])
                elif key in cosmo_dict["nuisance_params"]:
                    sub_vector.append(cosmo_dict["nuisance_params"][key]["value"])
                # special cases when bias parameters depend on other bias parameter values (TNS model)
                elif pname == "bs2" and cosmo_dict["nuisance_params"][pname]["value"] == -99:
                    sub_vector.append((-4./7)*(cosmo_dict["nuisance_params"]["b1"+"_"+str(isample)+"_"+str(iz)]["value"]-1))
                elif pname == "b3nl" and cosmo_dict["nuisance_params"][pname]["value"] == -99:
                    sub_vector.append((32./315)*(cosmo_dict["nuisance_params"]["b1"+"_"+str(isample)+"_"+str(iz)]["value"]-1))
                else:
                    sub_vector.append(cosmo_dict["nuisance_params"][pname]["value"])
            param_vector += sub_vector

    return np.array(param_vector)


def make_latin_hypercube(priors, N):
    """Generates a latin hypercube of N samples with lower and upper bounds given by priors"""

    n_dim = priors.shape[0]

    sampler = qmc.LatinHypercube(d=n_dim)
    params = sampler.random(n=N)

    for i in range(params.shape[1]):
        params[:,i] = (params[:,i] * (priors[i, 1] - priors[i, 0])) + priors[i,0]
    
    return params


def make_hypersphere(priors:np.array, dim:int, N:int):
    """Generates a hypersphere of N samples using the method from https://arxiv.org/abs/2405.01396v1
    
    Args:
        priors: (np.array): array of parameter minima and maxima. Should have shape (dim, 2)
        dim (int): number of parameters to generate a hypersphere with
        N (int): number of samples to uniformly generate within the hypersphere
    Returns:
        sphere_points (np.array): list of parameters uniformly sampled within a hypersphere. Has shape (N, dim)
    """

    # generate points in a uniform hypersphere with radius 1
    sphere_points = np.random.multivariate_normal(np.zeros(dim), np.eye(dim), size=N)
    radius = np.sqrt(np.sum(sphere_points**2, axis=1))[:, np.newaxis]
    uniform_points = np.random.uniform(0, 1, size=(N, 1))
    new_radius = uniform_points**(1./dim)
    sphere_points = (sphere_points / radius) * new_radius

    # expand each dimension to match the prior boundaries
    for d in range(dim):
        sphere_points[:,d] = ((sphere_points[:,d] + 1) * (priors[d, 1] - priors[d, 0]) / 2.) + priors[d,0]
    return sphere_points


def is_in_hypersphere(priors, params):
    """Returns whether or not the given params are within a hypersphere with edges defined by bounds"""

    if isinstance(priors, np.ndarray):
        priors = torch.from_numpy(priors)
    elif not isinstance(priors, torch.Tensor):
        raise TypeError(f"priors must be either np array or torch Tensor, but is {type(priors)}")

    if isinstance(params, np.ndarray):
        params = torch.from_numpy(params)
    elif not isinstance(params, torch.Tensor):
        raise TypeError(f"params must be either np array or torch Tensor, but is {type(params)}")
    unit_params = torch.zeros_like(params)

    # convert params to lay within the unit sphere
    if len(params.shape) == 1:
        for d in range(priors.shape[0]):
            unit_params[d] = 2*(params[d] - priors[d,0]) / (priors[d,1] - priors[d,0]) - 1
        r = torch.sqrt(torch.sum(unit_params**2))

    elif len(params.shape) == 2:
        for d in range(priors.shape[0]):
            unit_params[:,d] = 2*(params[:,d] - priors[d,0]) / (priors[d,1] - priors[d,0]) - 1
        r = torch.sqrt(torch.sum(unit_params**2, dim=1))

    return torch.lt(r, 1.0), r


def organize_training_set(training_dir:str, train_frac:float, valid_frac:float, test_frac:float, 
                          param_dim, num_zbins, num_spectra, num_ells, k_dim, remove_old_files=True):
    """Takes a set of matrices and reorganizes them into training, validation, and tests sets
    
    Args:
        training_dir: Directory contaitning matrices to organize
        train_frac: Fraction of dataset to partition as the training set
        valid_frac: Fraction of dataset to partition as the validation set
        test_frac: Fraction of dataset to partition as the test set
        param_dim: Dimension of input parameter arrays
        mat_dim: Dimention of power spectra
        remove_old_files: If True, deletes old data files after loading data into \
            memory and before re-organizing. Default True.
    """
    all_filenames = next(os.walk(training_dir), (None, None, []))[2]  # [] if no file

    all_params = np.array([], dtype=np.int64).reshape(0,param_dim)
    all_galaxy_ps = np.array([], dtype=np.int64).reshape(0, num_spectra, num_zbins, k_dim, num_ells)

    # load in all the data internally (NOTE: memory intensive!)
    # if "pk-raw.npz" in all_filenames:
    #     all_filenames = ["pk-raw.npz"]

    for file in all_filenames:
        if "pk-" in file:
            
            print("loading " + file + "...")
            F = np.load(training_dir+file)
            params = F["params"]
            galaxy_ps = F["galaxy_ps"]
            del F
            all_params = np.vstack([all_params, params])
            all_galaxy_ps = np.vstack([all_galaxy_ps, galaxy_ps])

    N = all_params.shape[0]
    N_train = int(N * train_frac)
    N_valid = int(N * valid_frac)
    N_test = int(N * test_frac)
    assert N_train + N_valid + N_test <= N

    valid_start = N_train
    valid_end = N_train + N_valid
    test_end = N_train + N_valid + N_test
    assert test_end - valid_end == N_test
    assert valid_end - valid_start == N_valid

    if remove_old_files == True:
        for file in all_filenames:
            if "pk-" in file: os.remove(training_dir+file)

    print("splitting dataset into chunks of size [{:0.0f}, {:0.0f}, {:0.0f}]...".format(N_train, N_valid, N_test))

    np.savez(training_dir+"pk-training.npz", 
                params=all_params[0:N_train],
                galaxy_ps=all_galaxy_ps[0:N_train])
    np.savez(training_dir+"pk-validation.npz", 
                params=all_params[valid_start:valid_end], 
                galaxy_ps=all_galaxy_ps[valid_start:valid_end])
    np.savez(training_dir+"pk-testing.npz", 
                params=all_params[valid_end:test_end], 
                galaxy_ps=all_galaxy_ps[valid_end:test_end]) 


def get_full_invcov(cov:torch.Tensor, num_zbins:int):
    """Calculates the full (multi-tracer) inverse covariance matrix given

    Args:
        cov (torch.Tensor): set of covariance matrices. Should have shape (num_zbins, X, X)
        num_zbins (int): number of redshift-bins. 

    Returns:
        invcov (torch.Tensor): Inverse covariance matrices. Has shape (num_zbins, X, X)
    """
    invcov = torch.zeros_like(cov)
    for z in range(num_zbins):
        invcov[z] = torch.linalg.inv(cov[z])
    return invcov


def get_invcov_blocks(cov:torch.Tensor, num_spectra:int, num_zbins:int, num_kbins:int, num_ells:int):
    """Calculates block inverse covariance matrices given a full multi-tracer covariance matrix.

    Args:
        cov (torch.Tensor): full block covariance matrix. Should have shape (num_zbins, num_spectra*num_kbins*num_ells, num_spectra*num_kbins*num_ells)
        num_spectra (int): number of (auto + cross) power spectra in the corresponding covariance matrix
        num_zbins (int): number of redshift bins in the corresponding covariance matrix
        num_kbins (int): number of k-mode bins in the corresponding covariance matrix
        num_ells (int): number of multipole moments in the corresponding covariance matrix

    Returns:
        invcov_blocks (torch.Tensor): Set of inverse block covariance matrices. Has shape (num_spectra, num_zbins, num_ells*num_kbins, num_ells*num_kbins)
    """
    invcov_blocks = torch.zeros((num_spectra, num_zbins, num_ells*num_kbins, num_ells*num_kbins)).to(torch.float64)

    for z in range(num_zbins):
        for ps in range(num_spectra):
            cov_sub = cov[z, ps*num_ells*num_kbins: (ps+1)*num_ells*num_kbins,\
                             ps*num_ells*num_kbins: (ps+1)*num_ells*num_kbins]
            invcov_blocks[ps, z] = torch.linalg.inv(cov_sub)

            try:
                L = torch.linalg.cholesky(invcov_blocks[ps, z])
            except:
                print("ERROR!, matrix block [{:d}, {:d}, {:d}] is not positive-definite!".format(z, ps, ps))

    return invcov_blocks


def mse_loss(predict:torch.Tensor, target:torch.Tensor, **args):
    """Calculates the mean-squared-error loss of the inputs.

    Args:
        predict (torch.Tensor): output of the network
        target (torch.Tensor): (batch of) elements in the training set. Should have the same shape as predict
        **args: extra arguments (needed by interface of ps_emulator)

    Returns:
        mse_loss: mean-squared-error loss of the given inputs
    """
    return F.mse_loss(predict, target, reduction="sum")


def hyperbolic_loss(predict, target, **args):
    """Calculates the hyperbolic loss of the inputs given by
    <sqrt(1 + 2(predict - target)**2)> - 1

    Args:
        predict (torch.Tensor): output of the network
        target (torch.Tensor): (batch of) elements in the training set. Should have the same shape as predict
        **args: extra arguments (needed by interface of ps_emulator)

    Returns:
        hyperbolic_loss: hyperbolic loss of the given inputs
    """
    return torch.mean(torch.sqrt(1 + 2*(predict - target)**2)) - 1


def hyperbolic_chi2_loss(predict:torch.Tensor, target:torch.Tensor, invcov:torch.Tensor, normalized=False):
    """Calculates the hyperbolic delta chi2 of the given inputs, which is given by the equation
    L = <sqrt(1 + 2(delta_chi_squared)> - 1

    Args:
        predict (torch.Tensor): output of the network
        target (torch.Tensor): (batch of) elements in the training set. Should have the same shape as predict
        invcov (torch.Tensor): either a full or block inverse covariance matrix, depending on whether the input is normalizeed or not
        normalized (bool, optional): whether or not the inputs are normalized. Defaults to False.

    Returns:
        hyperbolic_chi2 (torch.Tensor): mean hyperbolic chi2 of the given batch of inputs
    """
    chi2 = delta_chi_squared(predict, target, invcov, normalized)
    return torch.mean(torch.sqrt(1 + 2*chi2)) - 1


def delta_chi_squared(predict:torch.Tensor, target:torch.Tensor, invcov:torch.Tensor, normalized=False):
    """Calculates the delta chi squared of the given inputs, which is given by the equation,
    delta_chi2 = (predict - target)^T * invcov * (predict - target).
    
    Depending on whether the inputs are normalized, this function expects different shapes and cauclates 
    delta chi2 differenty. In either case however, the above equation applies.

    Args:
        predict (torch.Tensor): output of the emulator. Should have shape [b, 1, nl*nk] OR [nps, nz, nk, nl]
        target (torch.Tensor): data from the training / validation / test set. Should have shape [b, 1, nl*nk] OR [nps, nz, nk, nl]
        invcov (torch.Tensor): full inverse covariance matrix. Should have shape (z, nps*nl*nk, nps*nl*nk). Is only used if normalized == False
        normalized (bool, optional): Whether or not predict and target are normalized. Defaults to False.

    Raises:
        ValueError: if predict and target have different or unexpected shapes

    Returns:
        chi2 (torch.Tensor): delta_chi2 of the batch of inputs
    """
    if not isinstance(predict, torch.Tensor):
        predict = torch.from_numpy(predict).to(torch.float32).to(invcov.device)
    if not isinstance(target, torch.Tensor):
        target = torch.from_numpy(target).to(torch.float32).to(invcov.device)

    if target.device != invcov.device:  target = target.to(invcov.device)
    if predict.device != invcov.device: predict = predict.to(invcov.device)

    # inputs are size [b, 1, nl*nk]
    # OR [nps, nz, nk, nl] (same as cosmo_inference)
    if predict.shape != target.shape:
        raise ValueError("ERROR! preidciton and target shape mismatch: "+ str(predict.shape) +", "+ str(target.shape))
    delta = predict - target

    chi2 = 0
    # calculate the delta chi2 for the entire emulator output, assuming normalization has been undone
    if normalized == False:
        if delta.dim() == 2:
            chi2 += torch.matmul(delta, torch.matmul(invcov, delta.unsqueeze(2)))
        elif delta.dim() == 4:
            (nps, nz, nk, nl) = delta.shape
            for z in range(nz):
                chi2 += torch.matmul(delta[:,z].flatten(), 
                        torch.matmul(invcov[z], 
                        delta[:,z].flatten()))
        else:
            raise ValueError(f"Expected input data with 2 or 5 dimensions, but got {delta.dim()}")
    else:
        if delta.dim() == 1:
            delta = delta.unsqueeze(0)
            chi2 = torch.bmm(delta.unsqueeze(1), delta.unsqueeze(2)).squeeze()
        elif delta.dim() == 2:
            chi2 = torch.bmm(delta.unsqueeze(1), delta.unsqueeze(2)).squeeze()
        else:
            raise ValueError(f"Expected input data with 2 dimensions, but got {delta.dim()}")

    chi2 = torch.sum(chi2)
    return chi2


def calc_avg_loss(emulator, data_loader, loss_function:callable, bin_idx=None, mode="galaxy_ps"):
    """run thru the given data set and returns the average loss value for a given sub-network, or all sub-networks in a list

    Args:
        emulator (ps_emulator): emulator object to calculate the average loss with
        data_loader (dataLoader): Pytorch DataLoader object containing the data to loop over
        loss_function (callable): loss function to use
        bin_idx (list, optional): [ps, z] values to calculate the average loss for. If None, recuresively calls
            this function with all possible values of ps and z. Defaults to None
        mode (str, optional): which type of network to calculate the loss for (CURRENTLY HAS TO BE "galaxy_ps"!). Defaults to "galaxy_ps".

    Returns:
        total_loss (float or torch.Tensor): average loss corresponding to the net with bin_idx, or list of average loss for all sub-networks.
    """

    # if net_idx not specified, recursively call the function with all possible values
    if bin_idx == None and mode == "galaxy_ps":
        total_loss = torch.zeros(emulator.num_spectra, emulator.num_zbins, requires_grad=False)
        for (ps, z) in itertools.product(range(emulator.num_spectra), range(emulator.num_zbins)):
            total_loss[ps, z] = calc_avg_loss(emulator, data_loader, loss_function, [ps, z], mode)
        return total_loss
    
    emulator.galaxy_ps_model.eval()
    avg_loss = 0.
    with torch.no_grad():
        for (i, batch) in enumerate(data_loader):
            if mode == "galaxy_ps":
                params = emulator.galaxy_ps_model.organize_parameters(batch[0])
                params = normalize_cosmo_params(params, emulator.input_normalizations)
                prediction = emulator.galaxy_ps_model.forward(params, (bin_idx[1] * emulator.num_spectra) + bin_idx[0])
                target = torch.flatten(batch[1][:,bin_idx[0],bin_idx[1]], start_dim=1)
            else:
                raise KeyError(f"Invalid value for mode ({mode})")

            avg_loss += loss_function(prediction, target, emulator.invcov_blocks, True).item()

    return avg_loss / (len(data_loader.dataset))


def normalize_cosmo_params(params:torch.Tensor, normalizations:torch.Tensor):
    """Linearly normalizes input cosmology + bias parameters to lie within the range [0,1]

    Args:
        params (torch.Tensor): batch of input parameters to normalize. Should have shape [batch, num_spectra*num_zbins, num_cosmo_params + (num_nuisance_params)].
        normalizations (torch.Tensor): Tensor of parameter minima and maxima. Should have shape [2, num_spectra*num_zbins, num_cosmo_params + (num_nuisance_params)

    Returns:
        norm_params (torch.Tensor): batch of normalized input parameters. has shape [batch, num_spectra*num_zbins, num_cosmo_params + (num_nuisance_params)
    """
    return (params - normalizations[0]) / (normalizations[1] - normalizations[0])


def normalize_power_spectrum(ps_raw:torch.Tensor, ps_fid:torch.Tensor, sqrt_eigvals:torch.Tensor, Q:torch.Tensor):
    """Normalizes the given galaxy power spectrum multipoles using the method described in http://arxiv.org/abs/2403.12337

    Args:
        ps_raw (torch.Tensor): batch of power spectra in units of (Mpc/h)^3 to normalize. Should have shape [b, nps, z, nk*nl]
        ps_fid (torch.Tensor): fiducial power spectrum multipoles in units of (Mpc/h)^3 used for normalization. Should have shape [nps, z, nk*nl]
        sqrt_eigvals (torch.Tensor): set of sqrt eigenvalues used for normalization. Should have shape [ps, z, nk*nl]
        Q (torch.Tensor): set of eigenvectors used for normalization. Should have shape [ps, z, nk*nl, nk*nl]

    Returns:
        ps_norm: normalized power spectrum multipoles. Has shape [b, nps, z, nk*nl]
    """
    # assumes ps has shape [b, nps, z, nk*nl]
    ps_norm = torch.zeros_like(ps_raw)
    for (ps, z) in itertools.product(range(ps_norm.shape[1]), range(ps_norm.shape[2])):
        ps_norm[:,ps, z] = ((ps_raw[:, ps, z] @ Q[ps, z]) - (ps_fid[ps, z].flatten() @ Q[ps, z])) * sqrt_eigvals[ps, z]
    return ps_norm


def un_normalize_power_spectrum(ps_raw:torch.Tensor, ps_fid:torch.Tensor, sqrt_eigvals:torch.Tensor, Q:torch.Tensor, Q_inv:torch.Tensor):
    """Reverses normalization of a batch of output power spectru based on the method developed by http://arxiv.org/abs/2403.12337

    Args:
        ps (torch.Tensor): power spectrum to reverse normalization. Expected shape is either [nb, nps, nz, nk*nl] or [nb, 1, nk*nl]  
        ps_fid (torch.Tensor): fiducial power spectrum used to reverse normalization. Expected shape is [nps*nz, nk*nl]  
        sqrt_eigvals (torch.Tensor): square root eigenvalues of the inverse covariance matrix. Expected shape is [nps*nz, nk*nl]  
        Q (torch.Tensor): eigenvectors of the inverse covariance matrix. Expected shape is [nps*nz, nk*nl, nk*nl]  
        Q_inv (torch.Tensor): inverse eigenvectors of the inverse covariance matrix. Expected shape is [nps*nz, nk*nl, nk*nl]  
        net_idx (torch.Tensor): (optional) index specifying the specific sub-network output to reverse normalization. Default None. If not specified, will reverse normalization for the entire emulator output
    Returns:
        ps_new (torch.Tensor): galaxy power spectrum multipoles in units of (Mpc/h)^3 in the same shape as ps
    Raises:
        IndexError: If the given shape of ps_raw is invalid.
    """

    ps_new = torch.zeros_like(ps_raw)
    # assumes shape is [b, nps, nz, nk*nl]
    if len(ps_raw.shape) == 4:
        for (ps, z) in itertools.product(range(ps_new.shape[1]), range(ps_new.shape[2])):
            ps_new[:, ps, z] = (ps_raw[:, ps, z] / sqrt_eigvals[ps, z] + (ps_fid[ps, z] @ Q[ps, z])) @ Q_inv[ps, z]
    # assumes shape is [nps, nz, nk*nl]
    elif len(ps_raw.shape) == 3:
        for (ps, z) in itertools.product(range(ps_new.shape[0]), range(ps_new.shape[1])):
            ps_new[ps, z] = (ps_raw[ps, z] / sqrt_eigvals[ps, z] + (ps_fid[ps, z] @ Q[ps, z])) @ Q_inv[ps, z]
    else:
        raise IndexError(f"Incorrect input shape for ps_raw ({ps_raw.shape})!")

    return ps_new