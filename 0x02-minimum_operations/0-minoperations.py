#!/usr/bin/python3
"""this module finds the minimum operations to duplicate a letter in a file"""

from typing import List


def factorize(n: int) -> List[int]:
    """Return the prime factorization of n."""
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors


def minOperations(n: int) -> int:
    """Return the minimum number of operations to reach n from 1."""
    if n <= 1:
        return 0
    factors = factorize(n)
    return sum(factors)
