import torch
import os
import pytest

import mentat_lss.emulator as emulator
from mentat_lss.models.blocks import *

def test_linear_with_channels():
    # test that the linear_with_channels sub-block treats channels independently

    parallel_layers = linear_with_channels(10, 10, 2)
    with torch.no_grad():
        parallel_layers.w[0,:,:] = 1.
        parallel_layers.b[0,:,:] = 0.

    for n in range(100):
        test_input = torch.rand((1, 2, 10))
        test_output = parallel_layers(test_input)
        
        assert torch.all(test_output[:,1] != torch.sum(test_input[:,1]))

@pytest.mark.parametrize("input_dim, output_dim, num_layers, expected", [
    (10, 10, 2, None), 
    (1, 10, 3, None),
    (0, 10, 3, ValueError),
    (10, 0, 3, ValueError),
    (10, 10, 0, ValueError),
])
def test_block_resnet(input_dim, output_dim, num_layers, expected):

    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            resnet_block = block_resnet(input_dim, output_dim, num_layers, True)
    else:
        test_input = torch.rand((100, input_dim))
        resnet_block = block_resnet(input_dim, output_dim, num_layers, True)
        test_output = resnet_block(test_input)

        assert test_output.shape == (100, output_dim)
        assert not torch.all(torch.isnan(test_output))
        assert not torch.all(torch.isinf(test_output))

@pytest.mark.parametrize("embedding_dim, split_dim, expected", [
    (10, 10, None),
    (10, 5, None), 
    (2, 10, ValueError),
    (0, 10, ValueError),
    (10, 4, ValueError),
    (10, 0, ValueError),
])
def test_transformer_block(embedding_dim, split_dim, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            transformer_block = block_transformer_encoder(embedding_dim, split_dim, 0.1)
    else:
        transformer_block = block_transformer_encoder(embedding_dim, split_dim, 0.1)
        test_input = torch.rand(100, embedding_dim)
        test_output = transformer_block(test_input)

        assert test_output.shape == (100, embedding_dim)
        assert not torch.all(torch.isnan(test_output))
        assert not torch.all(torch.isinf(test_output))

def test_stacked_transformer_network():

    current_dir = os.path.dirname(os.path.realpath(__file__))
    test_dir = current_dir+"/../configs/network_pars/network_pars_example.yaml"

    # constructes the network
    test_emulator = emulator.ps_emulator(test_dir, "train")

    # generate a random input sequence and pass it through the network
    test_input = torch.randn(1, test_emulator.num_cosmo_params + \
                                (test_emulator.num_nuisance_params *test_emulator.num_zbins * test_emulator.num_tracers),
                                device = test_emulator.device)
    test_emulator.galaxy_ps_model.eval()
    test_input = test_emulator.galaxy_ps_model.organize_parameters(test_input)

    test_output_sub = test_emulator.galaxy_ps_model.forward(test_input, 0)
    test_output_full = test_emulator.galaxy_ps_model.forward(test_input)

    assert torch.all(torch.isnan(test_output_full)) == False
    assert torch.all(torch.isinf(test_output_full)) == False

    assert test_output_sub.shape == (1, test_emulator.num_kbins * test_emulator.num_ells)
    assert test_output_full.shape == (1, test_emulator.num_spectra,
                                         test_emulator.num_zbins,
                                         test_emulator.num_kbins*test_emulator.num_ells)
    assert torch.allclose(test_output_sub, test_output_full[:,0,0])