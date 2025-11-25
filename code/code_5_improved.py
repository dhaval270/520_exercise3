from __future__ import annotations
from typing import List


def candidate(numbers: List[float]) -> float:
    """Compute the mean absolute deviation (MAD) of a list of numbers.

    The mean absolute deviation is defined as:

        MAD(numbers) = (1 / n) * sum(|x - μ| for x in numbers)

    where
        n  = len(numbers)
        μ  = arithmetic mean of the list.

    For an empty list, this function returns 0.0 by convention.

    Parameters
    ----------
    numbers : List[float]
        A list of floating-point values.

    Returns
    -------
    float
        The mean absolute deviation of the input list.
    """
    # Handle the empty-input case explicitly to avoid division by zero.
    if not numbers:
        return 0.0

    n = len(numbers)
    mean = sum(numbers) / n

    mad = sum(abs(x - mean) for x in numbers) / n
    return mad
