from __future__ import annotations
from typing import List, Tuple


def candidate(numbers: List[int]) -> Tuple[int, int]:
    """Return the sum and product of a list of integers.

    The function returns a pair (S, P) where:
        S = sum(numbers)
        P = product(numbers)

    For the empty list, the result is defined as:
        S = 0   (additive identity)
        P = 1   (multiplicative identity).
    """
    total = sum(numbers)

    product = 1
    for value in numbers:
        product *= value

    return total, product
