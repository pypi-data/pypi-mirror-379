# mobius_activations/torch.py
import torch
import torch.nn as nn

class MobiusActivation(nn.Module):
    """
    A unified 3D activation function for PyTorch with a learnable mode.

    Operates as a fixed ReMU/S-ReMU or allows the network to learn the
    optimal geometric interference patterns for the data.
    """
    def __init__(self, realities=None, learnable=False, axes=['x', 'y', 'z']):
        """
        Initializes the MobiusActivation layer.

        Args:
            realities (list, optional): A list of reality dictionaries for fixed mode.
                                        Required if learnable=False. Defaults to None.
            learnable (bool, optional): If True, the layer will learn its own k and w
                                        parameters. Defaults to False.
            axes (list, optional): A list of axes to create learnable realities for.
                                   Only used if learnable=True. Defaults to ['x', 'y', 'z'].
        """
        super().__init__()
        self.learnable = learnable
        self._rotation_functions = {'x': self._rotate_x, 'y': self._rotate_y, 'z': self._rotate_z}

        if self.learnable:
            # --- LEARNABLE MODE ---
            if not axes:
                raise ValueError("The 'axes' argument must be provided in learnable mode.")
            self.axes = axes
            num_realities = len(axes)
            
            # Use nn.ParameterList to properly register learnable parameters with the model.
            # Initialize k with random values to break symmetry.
            # Initialize w with ones to give each reality equal starting influence.
            self.k_params = nn.ParameterList([nn.Parameter(torch.rand(1)) for _ in range(num_realities)])
            self.w_params = nn.ParameterList([nn.Parameter(torch.ones(1)) for _ in range(num_realities)])
            
            self.fixed_realities = None
            mode = "Learnable S-ReMU" if num_realities > 1 else "Learnable ReMU"
        else:
            # --- FIXED MODE ---
            if realities is None:
                raise ValueError("The 'realities' argument must be provided when learnable=False.")
            
            self.fixed_realities = realities
            self.k_params = None
            self.w_params = None
            self.axes = None
            mode = "Fixed S-ReMU" if len(realities) > 1 else "Fixed ReMU"

        print(f"PyTorch MobiusActivation initialized in {mode} mode.")


    def _rotate_z(self, z, k):
        mag = torch.linalg.norm(z, dim=1, keepdim=True) + 1e-8
        theta = k * mag
        cos_t, sin_t = torch.cos(theta), torch.sin(theta)
        
        a = torch.zeros_like(z)
        a[:, 0] = z[:, 0] * cos_t.squeeze() - z[:, 1] * sin_t.squeeze()
        a[:, 1] = z[:, 0] * sin_t.squeeze() + z[:, 1] * cos_t.squeeze()
        a[:, 2] = z[:, 2]
        return a

    def _rotate_y(self, z, k):
        mag = torch.linalg.norm(z, dim=1, keepdim=True) + 1e-8
        theta = k * mag
        cos_t, sin_t = torch.cos(theta), torch.sin(theta)
        
        a = torch.zeros_like(z)
        a[:, 0] = z[:, 0] * cos_t.squeeze() + z[:, 2] * sin_t.squeeze()
        a[:, 1] = z[:, 1]
        a[:, 2] = -z[:, 0] * sin_t.squeeze() + z[:, 2] * cos_t.squeeze()
        return a

    def _rotate_x(self, z, k):
        mag = torch.linalg.norm(z, dim=1, keepdim=True) + 1e-8
        theta = k * mag
        cos_t, sin_t = torch.cos(theta), torch.sin(theta)

        a = torch.zeros_like(z)
        a[:, 0] = z[:, 0]
        a[:, 1] = z[:, 1] * cos_t.squeeze() - z[:, 2] * sin_t.squeeze()
        a[:, 2] = z[:, 1] * sin_t.squeeze() + z[:, 2] * cos_t.squeeze()
        return a

    def forward(self, z):
        assert z.shape[1] == 3, f"Input must have 3 channels, but got {z.shape[1]}"
        
        if self.learnable:
            # Build the realities list dynamically from the learned parameters
            realities_to_use = []
            for i, axis in enumerate(self.axes):
                realities_to_use.append({
                    'axis': axis,
                    'k': self.k_params[i],
                    'w': self.w_params[i]
                })
        else:
            # Use the fixed realities provided during initialization
            realities_to_use = self.fixed_realities

        total_activation = torch.zeros_like(z)
        for reality in realities_to_use:
            rotation_func = self._rotation_functions[reality['axis']]
            transformed_z = rotation_func(z, reality['k'])
            total_activation += reality['w'] * transformed_z
            
        return total_activation


