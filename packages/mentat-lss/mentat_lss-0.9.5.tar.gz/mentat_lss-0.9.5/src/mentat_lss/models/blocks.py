import torch
import torch.nn as nn
from torch.nn import functional as F
import numpy as np


class linear_with_channels(nn.Module):
    """Class for independent MLP layers passed-through in parallel"""

    def __init__(self, input_dim:int, output_dim:int, num_channels:int):
        """Initializes a series of independent MLP layers based on the discussion at
        https://github.com/pytorch/pytorch/issues/36591.

        Args:
            input_dim (int): size of the input to the layer. Should be >0
            output_dim (int): size of the output of the layer. Should be >0
            num_channels (int): number of independent layers to create. Should be >1
        """
        super().__init__()
        
        self.w = nn.Parameter(torch.zeros(num_channels, input_dim, output_dim))
        self.b = nn.Parameter(torch.zeros(num_channels, 1, output_dim))

    def initialize_params(self, weight_initialization):
        """function for initializing layer weights, since pytorch struggles to do so automatically"""
        if weight_initialization == "He":
            torch.nn.init.kaiming_uniform_(self.w)
            fan_in, _ = torch.nn.init._calculate_fan_in_and_fan_out(self.w)
            bound = 1. / np.sqrt(fan_in)
            torch.nn.init.uniform_(self.b, -bound, bound)
        elif weight_initialization == "normal":
            nn.init.normal_(self.w, mean=0., std=0.1)
            nn.init.zeros_(self.b)
        elif weight_initialization == "xavier":
            nn.init.xavier_normal_(self.w)
        else: # if scheme is invalid, use normal initialization as a substitute
            nn.init.normal_(self.w, mean=0., std=0.1)
            nn.init.zeros_(self.w)

    def forward(self, X:torch.Tensor):
        """passes through the layer

        Args:
            X (torch.Tensor): Input to the layer. Should have shape (batch_size, num_channels, input_dim)

        Returns:
            X: (torch.Tensor): output of the layer. Has shape (batch_size, num_channels, output_dim)
        """

        # [b, c, in] x [b, in, out] = [b, c, out]
        # [c, b, in] x [c, in, out] = [c, b, out]
        X = X.permute(1, 0, 2) # <- [batch, channels, in] -> [channels, batch, in]
        X = torch.bmm(X, self.w) + self.b
        X = X.permute(1, 0, 2) # <- [channels, batch, out] -> [batch, channels, out]
        return X

class block_resnet(nn.Module):
    
    def __init__(self, input_dim:int, output_dim:int, num_layers:int, skip_connection:bool=True):
        """Initializes a resnet MLP block

        Args:
            input_dim (int): input dimension.
            output_dim (int): output dimension. All layers except for the first one will have this dimension
            num_layers (int): numer of layers to include in the block. Except for the first layer, will all have shape (output_dim, output_dim)
            skip_connection (bool, optional): whether to include a redidual connection, where the input is add
                to the output. Defaults to True.
        Raises:
            ValueError: If input_dim, output_dim, or num_layers are equal to 0
        """
        super().__init__()

        if input_dim <= 0 or output_dim <= 0 or num_layers <= 0:
            raise ValueError("Block structure parameters must be > 0")

        self.layers = nn.Sequential()
        self.layers.add_module("layer0",    nn.Linear(input_dim, output_dim))
        self.layers.add_module("Activation", activation_function(output_dim))
        for i in range(num_layers-1):
            self.layers.add_module("layer"+str(i+1), nn.Linear(output_dim, output_dim))
            self.layers.add_module("bn"+str(i+1),    nn.BatchNorm1d(output_dim))
            self.layers.add_module("Activation",     activation_function(output_dim))
    
        if skip_connection:
            self.skip_layer = nn.Linear(input_dim, output_dim)
            self.bn = nn.BatchNorm1d(output_dim)

    def forward(self, X:torch.Tensor):
        """Passes through the block

        Args:
            X (torch.Tensor): input to the block. Should have shape (batch_size, input_dim)

        Returns:
            X (torch.Tensor): output of the block. Has shape (batch_size, output_dim)
        """
        Y = self.layers(X)
        return Y + self.bn(self.skip_layer(X))

class block_parallel_resnet(nn.Module):
    
    def __init__(self, input_dim, output_dim, num_layers, num_channels, skip_connection):
        
        super().__init__()

        self.layers = nn.Sequential()
        self.layers.add_module("layer0",  linear_with_channels(input_dim, output_dim, num_channels))
        self.layers.add_module("ReLU",    nn.ReLU())
        for i in range(num_layers-1):
            self.layers.add_module("layer"+str(i+1), linear_with_channels(output_dim, output_dim, num_channels))
            self.layers.add_module("bn"+str(i+1),    nn.BatchNorm1d(num_channels))
            self.layers.add_module("ReLU",           nn.ReLU())
    
        if skip_connection:
            self.skip_layer = linear_with_channels(input_dim, output_dim, num_channels)
            self.bn = nn.BatchNorm1d(num_channels)

    def forward(self, X):
        Y = self.layers(X)
        return Y + self.bn(self.skip_layer(X))


class multi_headed_attention(nn.Module):

    def __init__(self, hidden_dim, num_heads=2, dropout_prob=0.):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.num_heads = num_heads

        self.layer_q = nn.Linear(hidden_dim, hidden_dim)
        self.layer_k = nn.Linear(hidden_dim, hidden_dim)
        self.layer_v = nn.Linear(hidden_dim, hidden_dim)
        self.out = nn.Linear(hidden_dim, hidden_dim)

        self.dropout = nn.Dropout(dropout_prob)
        #self.softmax = nn.Softmax(hidden_dim)

    def transpose_qkv(self, X):
        """Transposition for parallel computation of multiple attention heads."""
        # Shape of input X: (batch_size, no. of queries or key-value pairs, num_hiddens). 
        # Shape of output X: (batch_size, no. of queries or key-value pairs, num_heads, num_hiddens / num_heads)
        X = X.reshape(X.shape[0], X.shape[1], self.num_heads, -1)
        X = X.permute(0, 2, 1, 3)

        return X.reshape(-1, X.shape[2], X.shape[3])

    def transpose_output(self, X):
        """Reverse the operation of transpose_qkv."""
        X = X.reshape(-1, self.num_heads, X.shape[1], X.shape[2])
        X = X.permute(0, 2, 1, 3)
        return X.reshape(X.shape[0], X.shape[1], -1)

    def dot_product_attention(self, q, k, v):
        dim = q.shape[-1]
        # Swap the last two dimensions of keys with keys.transpose(1, 2)
        # calculate attention scores using the dot product
        scores = torch.bmm(q, k.transpose(1, 2)) / np.sqrt(dim)
        # normalize so that sum(scores) = 1 and all scores > 0
        #self.attention_weights = masked_softmax(scores, valid_lens)
        self.attention_weights = F.softmax(scores, dim=-1)
        # perform a batch matrix multiplaction to get the attention weights
        return torch.bmm(self.dropout(self.attention_weights), v)

    def forward(self, queries, keys, values):

        queries = self.transpose_qkv(self.layer_q(queries))
        keys    = self.transpose_qkv(self.layer_k(keys))
        values  = self.transpose_qkv(self.layer_v(values))

        X = self.dot_product_attention(queries, keys, values)
        X = X.reshape(-1, self.hidden_dim)
        X = self.out(X)
        return X

class block_addnorm(nn.Module):
    def __init__(self, shape, dropout_prob=0.):
        super().__init__()
        self.dropoiut = nn.Dropout(dropout_prob)
        self.layerNorm = nn.LayerNorm(shape)
    def forward(self, X, Y):
        return self.layerNorm(self.dropoiut(Y) + X)
    
class block_transformer_encoder(nn.Module):
    """Custom transformer encoder class"""

    def __init__(self, embedding_dim:int, split_dim:int, dropout_prob=0.):
        """Initializes the transformer encoder block

        Args:
            embedding_dim (int): size of the embedded input to the block. Should be divisible by split_dim
            split_dim (int): size of each independent feed-forward layer. Should be a factor of embedding_dim
            dropout_prob (float, optional): probability a given weight is dropped during training. Defaults to 0..

        Raises:
            ValueError: If hidden dim or split_dim are invalid. Both values must be > 0 and embedding_dim divisible by split_dim
        """
        super().__init__()
        self.embedding_dim = embedding_dim
        self.split_dim = split_dim
        self._check_inputs(embedding_dim, split_dim)

        #self.attention = multi_headed_attention(self.embedding_dim, 1, dropout_prob)
        self.attention = nn.MultiheadAttention(int(self.embedding_dim), 1, dropout_prob, batch_first=True)

        #feed-forward network
        self.h1 = linear_with_channels(int(self.embedding_dim/split_dim), int(self.embedding_dim/split_dim), split_dim)
        self.activation = activation_function(int(self.embedding_dim/split_dim))
        #self.addnorm2 = block_addnorm(self.embedding_dim, dropout_prob)

    def _check_inputs(self, embedding_dim, split_dim):
        """Checks the input block parameters are valid"""
        if embedding_dim <= 0 or split_dim <= 0:
            raise ValueError(f"All block structure parameters must be >= 0, but got embedding_dim={embedding_dim} and split_dim={split_dim}")
        if embedding_dim % split_dim != 0:
            raise ValueError(f"Embedding dim must be divisible by split_dim, but got a remainder of {embedding_dim % split_dim}")

    def forward(self, X:torch.Tensor):
        """Passes through the transformer block

        Args:
            X (torch.Tensor): Input to the block. Should have shape (batch_size, embedding_dim)

        Returns:
            X (torch.Tensor): Output of the block. Has shape (batch_size, embedding_dim)
        """
        X = torch.unsqueeze(X, 1)
        X = X + self.attention(X, X, X)[0]
        X = X.reshape(-1, X.shape[2])

        Y = X.reshape(-1, self.split_dim, int(self.embedding_dim / self.split_dim))
        Y = self.activation(self.h1(Y))
        X = X + Y.reshape(-1, self.embedding_dim)
        return X

class activation_function(nn.Module):
    """Custom nonlinear activation function"""

    def __init__(self, d:int):
        """Initializes a custom nonlinear activation function with equation,
        h(x) = [y + (1 + exp{-b * x}))^-1 * (1 - y)] * x, where y and b are trainable
        parameters.

        Args:
            d (int): dimension of the input to the function.
        """
        super().__init__()

        self.dim = d
        self.gamma = nn.Parameter(torch.zeros(d))
        self.beta = nn.Parameter(torch.zeros(d))

    def forward(self, X:torch.Tensor):
        """Passes through the activation function

        Args:
            X (torch.Tensor): Input to the function. Should be shape (batch_size, d)

        Returns:
           X (torch.Tensor): Output of the function. Has shape (batch_size, d)
        """
        inv = torch.special.expit(torch.mul(self.beta, X))
        return torch.mul(self.gamma + torch.mul(inv, 1-self.gamma), X)
