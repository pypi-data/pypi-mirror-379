# in tests/test_tensorflow.py

import tensorflow as tf
from tensorflow.keras import layers, Sequential
import numpy as np
import pytest

# Import your custom activation from the package
from mobius_activations.tensorflow import MobiusActivation

# ==============================================================================
# 1. Unit Tests: Testing the layer in isolation
# ==============================================================================

class TensorFlowUnitTests(tf.test.TestCase):
    
    def test_initialization_fixed(self):
        """Tests that the layer initializes correctly in fixed mode."""
        realities = [{'axis': 'x', 'k': 1.0, 'w': 1.0}]
        layer = MobiusActivation(realities=realities, learnable=False)
        self.assertFalse(layer.learnable)
        self.assertIsNotNone(layer.fixed_realities)

    def test_initialization_learnable(self):
        """Tests that the layer initializes correctly in learnable mode."""
        layer = MobiusActivation(learnable=True, axes=['x', 'z'])
        self.assertTrue(layer.learnable)
        # In TensorFlow, the weights are created during the build step
        # so we check the config instead of the created params directly
        self.assertEqual(len(layer.axes), 2)

    def test_initialization_errors(self):
        """Tests that the layer raises errors for invalid configurations."""
        with self.assertRaises(ValueError):
            MobiusActivation(learnable=False)
        with self.assertRaises(ValueError):
            MobiusActivation(learnable=True, axes=[])

    def test_shape_integrity(self):
        """Tests that the output shape is always the same as the input shape."""
        layer = MobiusActivation(learnable=True)
        input_tensor = tf.random.normal(shape=(16, 3))
        output_tensor = layer(input_tensor)
        self.assertShapeEqual(input_tensor.numpy(), output_tensor)

# ==============================================================================
# 2. Integration Tests: Testing within a Keras model
# ==============================================================================

class TensorFlowIntegrationTests(tf.test.TestCase):

    def test_keras_integration_and_gradients(self):
        """
        Tests if the layer works in a Keras Sequential model and that gradients
        flow through both the model weights and the learnable reality parameters.
        """

        tf.random.set_seed(42)
        model = Sequential([
            layers.Dense(3, input_shape=(10,)),
            MobiusActivation(learnable=True, axes=['x', 'y']),
            layers.Dense(1)
        ])
        input_data = tf.random.normal(shape=(4, 10))
        target = tf.random.normal(shape=(4, 1))
        
        with tf.GradientTape() as tape:
            output = model(input_data)
            loss = tf.keras.losses.MeanSquaredError()(target, output)
        
        gradients = tape.gradient(loss, model.trainable_variables)
        
        # Assert that gradients have been computed for all parameters
        self.assertEqual(len(gradients), 8)
        
        for grad in gradients:
            self.assertIsNotNone(grad)
        
        # Get the MobiusActivation layer from the model
        mobius_layer = model.layers[1]
        
        # Get the names of ONLY its trainable variables
        mobius_param_names = [p.name for p in mobius_layer.trainable_variables]
        
        # Assert that it has the correct number of parameters (k and w for x and y)
        self.assertEqual(len(mobius_param_names), 4)
        
        # Assert that the expected parameter names are present, regardless of order
        self.assertTrue(any('k_x' in name for name in mobius_param_names))
        self.assertTrue(any('w_x' in name for name in mobius_param_names))
        self.assertTrue(any('k_y' in name for name in mobius_param_names))
        self.assertTrue(any('w_y' in name for name in mobius_param_names))
        
        print("\nTF Integration Test Passed: Gradients flowed correctly.")
# ==============================================================================
# 3. Functional Tests: Formalizing our successful experiments
# ==============================================================================

def generate_spiral_data(n_points=200):
    """A smaller, faster version of the spiral generator for testing."""
    np.random.seed(42)
    n = n_points // 2
    theta = np.sqrt(np.random.rand(n)) * 3 * np.pi
    r_a = 2 * theta + np.pi
    data_a = np.array([np.cos(theta) * r_a, np.sin(theta) * r_a]).T
    r_b = -2 * theta - np.pi
    data_b = np.array([np.cos(theta) * r_b, np.sin(theta) * r_b]).T
    X = np.vstack([data_a, data_b])
    y = np.hstack([np.zeros(n), np.ones(n)]).reshape(-1, 1)
    return tf.constant(X, dtype=tf.float32), tf.constant(y, dtype=tf.float32)

class TensorFlowFunctionalTests(tf.test.TestCase):

    def test_functional_spiral_solver(self):
        """
        Tests if a Keras model with the learnable activation can achieve high
        accuracy on the spiral problem.
        """
        tf.random.set_seed(42)
        X_train, y_train = generate_spiral_data()

        model = Sequential([
            layers.Input(shape=(2,)),
            layers.Dense(3),
            layers.BatchNormalization(),
            MobiusActivation(learnable=True),
            layers.Dense(1, activation='sigmoid') # Use sigmoid for binary classification
        ])

        model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
                      loss='binary_crossentropy',
                      metrics=['accuracy'])

        # Train for a fixed number of epochs
        history = model.fit(X_train, y_train, epochs=500, verbose=0)

        # Evaluate the final accuracy
        loss, accuracy = model.evaluate(X_train, y_train, verbose=0)
        
        print(f"\nTF Functional Spiral Test Final Accuracy: {accuracy:.4f}")
        # Assert that the accuracy is very high, proving the model learned
        self.assertGreater(accuracy, 0.95)

# To run tests with pytest, it's helpful to have this at the end
if __name__ == '__main__':
    tf.test.main()
