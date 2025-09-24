import pytest
import torch
from philtorch.mat import companion
from philtorch.lti import linear_recurrence

from .test_lti_lfilter import _generate_random_signal
from .test_lti_ssm import _generate_random_filter_coeffs


@pytest.mark.parametrize(
    "device",
    [
        "cpu",
        pytest.param(
            "cuda",
            marks=pytest.mark.skipif(
                not torch.cuda.is_available(), reason="CUDA not available"
            ),
        ),
    ],
)
@pytest.mark.parametrize("batch", [True, False])
def test_lti_recur2_equiv(device: str, batch: bool):
    B = 3
    T = 101
    order = 2

    a = _generate_random_filter_coeffs(order, B if batch else 1)

    # Convert to torch tensors
    a_torch = torch.from_numpy(a).to(device)
    x_torch = torch.randn(B, T, order).to(device).to(dtype=a_torch.dtype)
    A = companion(a_torch).squeeze(0)

    zi = x_torch.new_zeros(B, order).normal_()

    lti_y = torch.ops.philtorch.lti_recur2(A, zi, x_torch)
    ltv_y = torch.ops.philtorch.recur2(
        A.unsqueeze(1).expand(-1, T, -1, -1) if batch else A.expand(T, -1, -1),
        zi,
        x_torch,
    )
    assert torch.allclose(lti_y, ltv_y), torch.max(torch.abs(lti_y - ltv_y))


@pytest.mark.parametrize("device", ["cpu"])
@pytest.mark.parametrize("batch", [True, False])
@pytest.mark.parametrize("order", [3, 5])
def test_lti_recurN_equiv(device: str, batch: bool, order: int):
    B = 4
    T = 101

    a = _generate_random_filter_coeffs(order, B if batch else 1)

    # Convert to torch tensors
    a_torch = torch.from_numpy(a).to(device)
    x_torch = torch.randn(B, T, order).to(device).to(dtype=a_torch.dtype)
    A = companion(a_torch).squeeze(0)

    zi = x_torch.new_zeros(B, order).normal_()

    lti_y = torch.ops.philtorch.lti_recurN(A, zi, x_torch)
    ltv_y = torch.ops.philtorch.recurN(
        A.unsqueeze(1).expand(-1, T, -1, -1) if batch else A.expand(T, -1, -1),
        zi,
        x_torch,
    )
    assert torch.allclose(lti_y, ltv_y)


@pytest.mark.parametrize(
    "device",
    [
        "cpu",
        pytest.param(
            "cuda",
            marks=pytest.mark.skipif(
                not torch.cuda.is_available(), reason="CUDA not available"
            ),
        ),
    ],
)
@pytest.mark.parametrize("batch", [True, False])
def test_lti_recur_equiv(device: str, batch: bool):
    B = 3
    T = 101

    # Convert to torch tensors
    a_torch = torch.rand(B if batch else 1).to(device).double() * 2 - 1
    x_torch = torch.randn(B, T).to(device).double()
    zi = x_torch.new_zeros(B).normal_()

    lti_y = torch.ops.philtorch.lti_recur(a_torch, zi, x_torch)
    torch_y = linear_recurrence(a_torch, zi, x_torch)
    assert torch.allclose(lti_y, torch_y), torch.max(torch.abs(lti_y - torch_y))
