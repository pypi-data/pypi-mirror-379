# mobius_activations/tensorflow.py
import tensorflow as tf
from tensorflow.keras import layers

class MobiusActivation(layers.Layer):
    """
    A unified 3D activation function for TensorFlow/Keras, operating as a 
    Rectified Möbius Unit (ReMU) or a Superposition ReMU (S-ReMU). with a learnable mode.

    Inherits from tf.keras.layers.Layer for seamless Keras integration.
    """
    def __init__(self, realities=None, learnable=False, axes=['x', 'y', 'z'], **kwargs):
        super().__init__(**kwargs)
        self.learnable = learnable
        self.axes = axes
        self.fixed_realities = realities
        
        if self.learnable and not axes:
            raise ValueError("The 'axes' argument must be provided in learnable mode.")
        if not self.learnable and realities is None:
            raise ValueError("The 'realities' argument must be provided when learnable=False.")
            
        self._rotation_functions = {'x': self._rotate_x, 'y': self._rotate_y, 'z': self._rotate_z}

    def build(self, input_shape):
        if self.learnable:
            # Create learnable weights using the Keras-native add_weight method
            self.k_params = []
            self.w_params = []
            for axis in self.axes:
                self.k_params.append(self.add_weight(
                    name=f'k_{axis}', shape=(1,), initializer='random_uniform', trainable=True
                ))
                self.w_params.append(self.add_weight(
                    name=f'w_{axis}', shape=(1,), initializer='ones', trainable=True
                ))
        super().build(input_shape) # Standard practice to call this at the end

    def _rotate_z(self, z, k):
        mag = tf.linalg.norm(z, axis=1, keepdims=True) + 1e-8
        theta = k * mag
        cos_t, sin_t = tf.cos(theta), tf.sin(theta)
        
        a = tf.concat([
            z[:, 0:1] * cos_t - z[:, 1:2] * sin_t,
            z[:, 0:1] * sin_t + z[:, 1:2] * cos_t,
            z[:, 2:3]
        ], axis=1)
        return a

    def _rotate_y(self, z, k):
        mag = tf.linalg.norm(z, axis=1, keepdims=True) + 1e-8
        theta = k * mag
        cos_t, sin_t = tf.cos(theta), tf.sin(theta)
        
        a = tf.concat([
            z[:, 0:1] * cos_t + z[:, 2:3] * sin_t,
            z[:, 1:2],
            -z[:, 0:1] * sin_t + z[:, 2:3] * cos_t
        ], axis=1)
        return a

    def _rotate_x(self, z, k):
        mag = tf.linalg.norm(z, axis=1, keepdims=True) + 1e-8
        theta = k * mag
        cos_t, sin_t = tf.cos(theta), tf.sin(theta)
        
        a = tf.concat([
            z[:, 0:1],
            z[:, 1:2] * cos_t - z[:, 2:3] * sin_t,
            z[:, 1:2] * sin_t + z[:, 2:3] * cos_t
        ], axis=1)
        return a

    def call(self, z):
        tf.Assert(tf.equal(tf.shape(z)[1], 3), [f"Input must have 3 channels, but got {tf.shape(z)[1]}"])
        
        if self.learnable:
            # Build the realities list dynamically from the learned weights
            realities_to_use = []
            for i, axis in enumerate(self.axes):
                realities_to_use.append({
                    'axis': axis,
                    'k': self.k_params[i],
                    'w': self.w_params[i]
                })
        else:
            # Use the fixed realities
            realities_to_use = self.fixed_realities
            
        total_activation = tf.zeros_like(z)
        for reality in realities_to_use:
            rotation_func = self._rotation_functions[reality['axis']]
            transformed_z = rotation_func(z, reality['k'])
            total_activation += reality['w'] * transformed_z
            
        return total_activation
