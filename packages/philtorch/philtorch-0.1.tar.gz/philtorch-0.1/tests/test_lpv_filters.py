import pytest
import numpy as np
import torch
from typing import Tuple
from scipy import signal

from philtorch.lpv import lfilter, allpole as lpv_allpole, fir as lpv_fir
from .test_lpv_lfilter import _generate_random_signal


@pytest.mark.parametrize("B", [1, 8])
@pytest.mark.parametrize("T", [64])
@pytest.mark.parametrize("order", [1, 2, 4])
def test_allpole_inverse(B: int, T: int, order: int):
    """Test all-pole filter inverse operation"""
    a = torch.randn(B, T, order).double()
    a = a / a.abs().sum(dim=-1, keepdim=True).clamp(min=1e-6)  # Ensure stability
    x = torch.randn(B, T).double()
    zi = torch.randn(B, order).double()

    # Apply all-pole filter
    y, _ = lpv_allpole(a, x, zi=zi)

    # Inverse all-pole filter
    b = torch.cat([torch.ones(B, T, 1), a], dim=-1)  # FIR coefficients from all-pole
    x_reconstructed, _ = lpv_fir(b, y, zi=zi)

    assert x.shape == x_reconstructed.shape, "Reconstructed signal shape mismatch"
    assert torch.allclose(x, x_reconstructed), "Reconstructed signal mismatch"


@pytest.mark.parametrize("B", [1, 8])
@pytest.mark.parametrize("T", [64])
@pytest.mark.parametrize("order", [1, 2, 4])
def test_fir_inverse(B: int, T: int, order: int):
    """Test FIR filter inverse operation"""
    a = torch.randn(B, T, order).double()
    a = a / a.abs().sum(dim=-1, keepdim=True).clamp(min=1e-6)
    g0 = torch.randn(B, T, 1).double()
    b = torch.cat([g0, a * g0], dim=-1)
    x = torch.randn(B, T).double()
    zi = torch.zeros(B, order).double()

    # Apply FIR filter
    y, _ = lpv_fir(b, x, zi=zi)

    # Inverse FIR filter
    x_reconstructed, _ = lpv_allpole(a, y / g0.squeeze(2), zi=zi)
    assert x.shape == x_reconstructed.shape, "Reconstructed signal shape mismatch"
    assert torch.allclose(x, x_reconstructed), "Reconstructed signal mismatch"


def _generate_time_varying_coeffs(
    B: int,
    T: int,
    num_order: int,
    den_order: int,
) -> Tuple[torch.Tensor, torch.Tensor]:
    """Generate time-varying filter coefficients"""
    # Generate smooth time-varying coefficients
    b = torch.randn(B, T, num_order + 1)
    a = torch.randn(B, T, den_order)

    # Ensure stability by keeping denominator coefficients small
    # a = torch.clamp(a, -0.5, 0.5)
    a = a / a.abs().sum(dim=-1, keepdim=True).clamp(min=1e-6)

    return b, a


def _generate_test_signal(
    B: int, T: int, signal_type: str = "white_noise"
) -> torch.Tensor:
    """Generate different types of test signals"""
    if signal_type == "white_noise":
        return torch.randn(B, T)
    elif signal_type == "impulse":
        x = torch.zeros(B, T)
        x[:, 0] = 1.0
        return x
    elif signal_type == "step":
        return torch.ones(B, T)
    elif signal_type == "sine":
        t = torch.linspace(0, 4 * np.pi, T).unsqueeze(0).expand(B, -1)
        return torch.sin(t)
    else:
        raise ValueError(f"Unknown signal type: {signal_type}")


@pytest.mark.parametrize("B", [1, 8, 16])
@pytest.mark.parametrize("T", [32, 128])
@pytest.mark.parametrize("num_order", [1, 2, 4])
@pytest.mark.parametrize("den_order", [1, 3, 5])
@pytest.mark.parametrize("form", ["df1", "df2"])
def test_time_varying_basic_functionality(
    B: int, T: int, num_order: int, den_order: int, form: str
):
    """Test basic functionality with time-varying coefficients"""
    b, a = _generate_time_varying_coeffs(B, T, num_order, den_order)
    x = _generate_test_signal(B, T, "white_noise")

    y = lfilter(b, a, x, form=form)

    if isinstance(y, tuple):
        y, zf = y
        assert zf.shape[0] == B  # Check final state shape

    assert y.shape == (B, T)
    assert not torch.isnan(y).any(), f"NaN values found in output for form {form}"
    assert torch.isfinite(y).all(), f"Non-finite values found in output for form {form}"


@pytest.mark.parametrize("signal_type", ["impulse", "step", "sine", "white_noise"])
def test_different_input_signals(signal_type: str):
    """Test filter response to different input signal types"""
    B, T = 2, 100
    b, a = _generate_time_varying_coeffs(B, T, 3, 2)
    x = _generate_test_signal(B, T, signal_type)

    y = lfilter(b, a, x, form="df1")

    if isinstance(y, tuple):
        y = y[0]

    assert y.shape == (B, T)
    assert not torch.isnan(y).any()
    assert torch.isfinite(y).all()

    # For impulse response, check that it's not all zeros
    if signal_type == "impulse":
        assert not torch.allclose(y, torch.zeros_like(y))


def test_linearity_property():
    """Test linearity: filter(a*x1 + b*x2) = a*filter(x1) + b*filter(x2)"""
    B, T = 2, 50
    b, a = _generate_time_varying_coeffs(B, T, 2, 1)
    b, a = b.double(), a.double()

    x1 = _generate_test_signal(B, T, "white_noise").double()
    x2 = _generate_test_signal(B, T, "white_noise").double()

    alpha, beta = 0.7, 1.3
    x_combined = alpha * x1 + beta * x2

    y1 = lfilter(b, a, x1, form="df1")
    y2 = lfilter(b, a, x2, form="df1")
    y_combined = lfilter(b, a, x_combined, form="df1")

    # Extract tensor from tuple if necessary
    if isinstance(y1, tuple):
        y1 = y1[0]
    if isinstance(y2, tuple):
        y2 = y2[0]
    if isinstance(y_combined, tuple):
        y_combined = y_combined[0]

    y_expected = alpha * y1 + beta * y2

    # Check linearity within reasonable tolerance
    assert torch.allclose(y_combined, y_expected)


def test_zero_input_zero_output():
    """Test that zero input produces zero output (assuming zero initial conditions)"""
    B, T = 2, 50
    b, a = _generate_time_varying_coeffs(B, T, 2, 1)
    x = torch.zeros(B, T)

    y = lfilter(b, a, x, form="df1")

    if isinstance(y, tuple):
        y = y[0]

    assert torch.allclose(y, torch.zeros_like(y))


def test_batch_independence():
    """Test that different batches are processed independently"""
    B, T = 3, 50

    # Create different coefficients for each batch
    b = torch.randn(B, T, 3) * 0.1
    a = torch.randn(B, T, 2) * 0.1

    # Create different inputs for each batch
    x = torch.randn(B, T)

    # Process all batches together
    y_batch = lfilter(b, a, x, form="df1")

    if isinstance(y_batch, tuple):
        y_batch = y_batch[0]

    # Process each batch individually
    y_individual = []
    for i in range(B):
        y_i = lfilter(b[i : i + 1], a[i : i + 1], x[i : i + 1], form="df1")
        if isinstance(y_i, tuple):
            y_i = y_i[0]
        y_individual.append(y_i)

    y_individual = torch.cat(y_individual, dim=0)

    # Results should be identical
    assert torch.allclose(y_batch, y_individual)


def test_initial_conditions_df2():
    """Test filter with initial conditions in DF2 form"""
    B, T = 2, 50
    order = 3
    b, a = _generate_time_varying_coeffs(B, T, order, order)
    x = _generate_test_signal(B, T, "white_noise")

    # Test with random initial conditions
    zi = torch.randn(B, order) * 0.1

    y, zf = lfilter(b, a, x, zi=zi, form="df2")

    assert y.shape == (B, T)
    assert zf.shape == (B, order)
    assert not torch.isnan(y).any()
    assert not torch.isnan(zf).any()
    assert torch.isfinite(y).all()
    assert torch.isfinite(zf).all()


def test_df_fir():
    """Test df2 filter with FIR coefficients"""

    B = 3
    T = 100
    num_order = 4

    b = np.random.randn(B, num_order + 1)
    x = _generate_random_signal(B, T)

    # Convert to torch tensors
    b_torch = torch.from_numpy(b)
    x_torch = torch.from_numpy(x)

    # Apply philtorch filter
    y_torch = lpv_fir(b_torch.unsqueeze(1).expand(-1, T, -1), x_torch, transpose=False)
    # Apply scipy filter
    y_scipy = np.stack([signal.lfilter(b[i], [1.0], x[i]) for i in range(B)], axis=0)

    # Compare outputs
    assert np.allclose(y_torch.numpy(), y_scipy), np.max(
        np.abs(y_torch.numpy() - y_scipy)
    )


def test_df_allpole():
    """Test df2 filter with all-pole coefficients"""

    B = 3
    T = 100
    num_order = 4

    a = np.random.randn(B, num_order)
    a /= np.abs(a).sum(axis=-1, keepdims=True).clip(min=1e-6)  # Ensure stability
    x = _generate_random_signal(B, T)

    # Convert to torch tensors
    a_torch = torch.from_numpy(a)
    x_torch = torch.from_numpy(x)

    # Apply philtorch filter
    y_torch = lpv_allpole(
        a_torch.unsqueeze(1).expand(-1, T, -1), x_torch, transpose=False
    )
    # Apply scipy filter
    y_scipy = np.stack(
        [signal.lfilter([1.0], [1.0] + a[i].tolist(), x[i]) for i in range(B)], axis=0
    )

    # Compare outputs
    assert np.allclose(y_torch.numpy(), y_scipy), np.max(
        np.abs(y_torch.numpy() - y_scipy)
    )


@pytest.mark.parametrize("include_zi", [True, False])
def test_tdf_fir(include_zi: bool):
    """Test df2 filter with FIR coefficients"""

    B = 3
    T = 100
    num_order = 4

    b = np.random.randn(B, num_order + 1)
    x = _generate_random_signal(B, T)
    if include_zi:
        # Generate random initial conditions
        zi = np.random.randn(B, num_order)
    else:
        zi = None

    # Convert to torch tensors
    b_torch = torch.from_numpy(b)
    x_torch = torch.from_numpy(x)
    if zi is not None:
        zi_torch = torch.from_numpy(zi)
    else:
        zi_torch = None

    # Apply philtorch filter
    torch_results = lpv_fir(
        b_torch.unsqueeze(1).expand(-1, T, -1), x_torch, zi=zi_torch, transpose=True
    )
    # Apply scipy filter
    scipy_results = [
        signal.lfilter(b[i], [1.0], x[i], zi=zi[i] if zi is not None else None)
        for i in range(B)
    ]

    if include_zi:
        y_scipy, zf_scipy = zip(*scipy_results)
        y_scipy = np.stack(y_scipy, axis=0)
        zf_scipy = np.stack(zf_scipy, axis=0)
        y_torch, zf_torch = torch_results

        assert np.allclose(zf_torch.numpy(), zf_scipy), np.max(
            np.abs(zf_torch.numpy() - zf_scipy)
        )
    else:
        y_scipy = np.vstack(scipy_results)
        y_torch = torch_results

    # Compare outputs
    assert np.allclose(y_torch.numpy(), y_scipy), np.max(
        np.abs(y_torch.numpy() - y_scipy)
    )


@pytest.mark.parametrize("include_zi", [True, False])
def test_tdf_allpole(include_zi: bool):
    """Test df2 filter with FIR coefficients"""

    B = 3
    T = 100
    num_order = 4

    a = np.random.randn(B, num_order)
    a /= np.abs(a).sum(axis=-1, keepdims=True).clip(min=1e-6)  # Ensure stability
    x = _generate_random_signal(B, T)
    if include_zi:
        # Generate random initial conditions
        zi = np.random.randn(B, num_order)
    else:
        zi = None

    # Convert to torch tensors
    a_torch = torch.from_numpy(a)
    x_torch = torch.from_numpy(x)
    if zi is not None:
        zi_torch = torch.from_numpy(zi)
    else:
        zi_torch = None

    # Apply philtorch filter
    torch_results = lpv_allpole(
        a_torch.unsqueeze(1).expand(-1, T, -1), x_torch, zi=zi_torch, transpose=True
    )
    # Apply scipy filter
    scipy_results = [
        signal.lfilter(
            [1.0], [1.0] + a[i].tolist(), x[i], zi=zi[i] if zi is not None else None
        )
        for i in range(B)
    ]

    if include_zi:
        y_scipy, zf_scipy = zip(*scipy_results)
        y_scipy = np.stack(y_scipy, axis=0)
        zf_scipy = np.stack(zf_scipy, axis=0)
        y_torch, zf_torch = torch_results

        assert np.allclose(zf_torch.numpy(), zf_scipy), np.max(
            np.abs(zf_torch.numpy() - zf_scipy)
        )
    else:
        y_scipy = np.vstack(scipy_results)
        y_torch = torch_results

    # Compare outputs
    assert np.allclose(y_torch.numpy(), y_scipy), np.max(
        np.abs(y_torch.numpy() - y_scipy)
    )


@pytest.mark.parametrize("transpose", [True, False])
@pytest.mark.parametrize("filt", [lpv_fir, lpv_allpole])
def test_zi_continuation(filt, transpose: bool):
    """Test that final state can be used to continue filtering"""
    B, T = 2, 27
    b, a = _generate_time_varying_coeffs(B, T, 3, 3)
    b, a = b.double(), a.double()
    if filt == lpv_fir:
        coef = b
    else:
        coef = a
    x = _generate_test_signal(B, T, "white_noise").double()

    # First pass with initial conditions
    zi = torch.randn(B, 3).double() * 0.1
    y1, zf1 = filt(coef, x, zi=zi, transpose=transpose)

    y2 = []
    for xn, coef_n in zip(x.chunk(3, dim=1), coef.chunk(3, dim=1)):
        yn, zf = filt(coef_n, xn, zi=zi, transpose=transpose)
        zi = zf
        y2.append(yn)
    y2 = torch.cat(y2, dim=1)

    assert y1.shape == y2.shape, "Output shape mismatch between passes"
    assert torch.allclose(y1, y2), "Output mismatch between passes"
    assert torch.allclose(zf1, zf), "Final state mismatch between passes"
