from typing import Annotated, Protocol, TypeAlias, runtime_checkable

import numpy as np
from pydantic import AfterValidator, ConfigDict, validate_call


# Validators
def is_matrix(x: np.ndarray) -> np.ndarray:
    """Checks if the argument is a matrix.

    Args:
        x (np.ndarray): The input array.

    Raises:
        ValueError: If the array is not a matrix.

    Returns:
        np.ndarray: The output array.
    """
    if x.ndim != 2:
        raise ValueError(f"Expected matrix, got {x.ndim}-dimensional array")
    return x


def is_strict_pos(x: int | float) -> int | float:
    """Checks if the argument is strictly positive.

    Args:
        x (int | float): The input number.

    Raises:
        ValueError: If the number is not strictly positive.

    Returns:
        int | float | torch.Tensor: The output number or tensor.
    """
    if x <= 0:
        raise ValueError(f"Expected strictly positive number, got {x}")
    return x


def is_gt_zero_lt_half(x: float) -> float:
    """Checks if the argument is between 0 and 1/2.

    Args:
        x (float): The input number.

    Raises:
        ValueError: If the number is not between 0 and 1/2.

    Returns:
        float: The output number.
    """
    if x <= 0 or x >= 0.5:  # noqa: PLR2004
        raise ValueError(f"Expected number > 0 and < 1/2, got {x}")
    return x


# Type annotations
Matrix: TypeAlias = Annotated[np.ndarray, AfterValidator(is_matrix)]
Num: TypeAlias = int | float
IntStrictlyPositive = Annotated[int, AfterValidator(is_strict_pos)]
NumStrictlyPositive = Annotated[Num, AfterValidator(is_strict_pos)]
FloatGtZeroLtHalf = Annotated[float, AfterValidator(is_gt_zero_lt_half)]


# Protocols
@runtime_checkable
class AffinityTransform(Protocol):
    """Protocol for affinity transforms.

    Use this protocol to define custom affinity transforms.
    """

    def __call__(self, x: np.ndarray) -> np.ndarray: ...


# Transformations
class ExpQuantileTransform(AffinityTransform):
    """Exponential quantile transform.

    Attributes:
        alpha (float): Quantile for affinity matrix computation.
        mult_factor (int | float): Scaling parameter for affinity matrix computation.
    """

    alpha: float
    mult_factor: int | float

    @validate_call(config=ConfigDict(arbitrary_types_allowed=True))
    def __init__(
        self, alpha: FloatGtZeroLtHalf = 0.1, mult_factor: NumStrictlyPositive = 1e4
    ):
        """Initialize the Exponential quantile transform.

        Args:
            alpha (FloatGtZeroLtHalf): Quantile for affinity matrix computation.
            mult_factor (NumStrictlyPositive): Scaling parameter for affinity matrix
                computation.
        """
        self.alpha = alpha
        self.mult_factor = mult_factor

    def __call__(self, x: np.ndarray) -> np.ndarray:
        q1, q2 = np.quantile(x, [self.alpha, 1 - self.alpha])
        gamma = np.log(self.mult_factor) / (q2 - q1)
        return np.exp(gamma * (x - x.max()))
