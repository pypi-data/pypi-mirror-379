# in tests/test_torch.py

import torch
import torch.nn as nn
import pytest  # Make sure to pip install pytest

# Import your custom activation from the package
from mobius_activations.torch import MobiusActivation

# ==============================================================================
# 1. Unit Tests: Testing the layer in isolation
# ==============================================================================

def test_initialization_fixed():
    """Tests that the layer initializes correctly in fixed mode."""
    realities = [{'axis': 'x', 'k': 1.0, 'w': 1.0}]
    layer = MobiusActivation(realities=realities, learnable=False)
    assert not layer.learnable
    assert layer.fixed_realities is not None

def test_initialization_learnable():
    """Tests that the layer initializes correctly in learnable mode."""
    layer = MobiusActivation(learnable=True, axes=['x', 'z'])
    assert layer.learnable
    assert len(layer.k_params) == 2
    assert len(layer.w_params) == 2

def test_initialization_errors():
    """Tests that the layer raises errors for invalid configurations."""
    # Should fail if learnable=False and no realities are provided
    with pytest.raises(ValueError):
        MobiusActivation(learnable=False)
    
    # Should fail if learnable=True and no axes are provided
    with pytest.raises(ValueError):
        MobiusActivation(learnable=True, axes=[])

def test_shape_integrity():
    """Tests that the output shape is always the same as the input shape."""
    layer = MobiusActivation(learnable=True)
    # Input is (Batch Size, Features) -> (16, 3)
    input_tensor = torch.randn(16, 3)
    output_tensor = layer(input_tensor)
    assert input_tensor.shape == output_tensor.shape

# ==============================================================================
# 2. Integration Tests: Testing within a PyTorch model
# ==============================================================================

def test_pytorch_integration_and_gradients():
    """
    Tests if the layer works in nn.Sequential and that gradients flow
    through both the model weights and the learnable reality parameters.
    """
    # Set a seed for repeatability
    torch.manual_seed(42)

    model = nn.Sequential(
        nn.Linear(10, 3),
        MobiusActivation(learnable=True, axes=['x', 'y']),
        nn.Linear(3, 1)
    )
    
    input_data = torch.randn(4, 10)
    target = torch.randn(4, 1)
    
    # Check that learnable parameters exist
    mobius_layer = model[1]
    assert mobius_layer.k_params[0].requires_grad
    assert mobius_layer.w_params[0].requires_grad
    
    # Perform a backward pass
    output = model(input_data)
    loss = nn.MSELoss()(output, target)
    loss.backward()
    
    # Assert that gradients have been computed for all parameters
    assert model[0].weight.grad is not None
    assert mobius_layer.k_params[0].grad is not None
    assert mobius_layer.w_params[0].grad is not None
    assert model[2].weight.grad is not None
    print("\nIntegration Test Passed: Gradients flowed correctly.")

# ==============================================================================
# 3. Functional Tests: Formalizing our successful experiments
# ==============================================================================

def generate_spiral_data(n_points=200):
    """A smaller, faster version of the spiral generator for testing."""
    torch.manual_seed(42)
    n = n_points // 2
    theta = torch.sqrt(torch.rand(n)) * 3 * torch.pi
    r_a = 2 * theta + torch.pi
    data_a = torch.stack([torch.cos(theta) * r_a, torch.sin(theta) * r_a], 1)
    r_b = -2 * theta - torch.pi
    data_b = torch.stack([torch.cos(theta) * r_b, torch.sin(theta) * r_b], 1)
    X = torch.cat([data_a, data_b], 0)
    y = torch.cat([torch.zeros(n), torch.ones(n)], 0).view(-1, 1)
    return X, y

def test_functional_spiral_solver():
    """
    Tests if a model with the learnable activation can achieve high accuracy
    on the spiral problem. This codifies our experiment into a pass/fail test.
    """
    torch.manual_seed(42)
    X_train, y_train = generate_spiral_data()

    model = nn.Sequential(
        nn.Linear(2, 3),
        nn.BatchNorm1d(3),
        MobiusActivation(learnable=True),
        nn.Linear(3, 1)
    )

    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    loss_fn = nn.BCEWithLogitsLoss()

    # Train for a fixed number of epochs
    for _ in range(500):
        optimizer.zero_grad()
        output = model(X_train)
        loss = loss_fn(output, y_train)
        loss.backward()
        optimizer.step()

    # Evaluate the final accuracy
    with torch.no_grad():
        preds = torch.sigmoid(model(X_train)) > 0.5
        accuracy = (preds.float() == y_train).float().mean()

    print(f"\nFunctional Spiral Test Final Accuracy: {accuracy.item():.4f}")
    # Assert that the accuracy is very high, proving the model learned
    assert accuracy > 0.95
