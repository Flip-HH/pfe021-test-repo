"""Examples of functions with varying algorithmic complexity.

This module contains short, self-contained functions illustrating
different time/space complexities: O(1), O(n), O(n^2), O(log n),
O(n log n), recursion, generators, and a simple async example.
"""

from typing import Iterable, List, Generator, Optional
import math
import asyncio

# TODO
def constant_time(value: int) -> int:
    """O(1) - return the input unchanged."""
    return value

# BUGfix
def linear_sum(values: Iterable[int]) -> int:
    """O(n) - sum all values in an iterable."""
    total = 0
    for v in values:
        total += v
    return total

# FixMe
def quadratic_pair_sums(values: List[int]) -> List[int]:
    """O(n^2) - return sums for every ordered pair (i, j).

    For a list of length n this produces n*n sums.
    """
    out: List[int] = []
    n = len(values)
    for i in range(n):
        for j in range(n):
            out.append(values[i] + values[j])
    return out


def binary_search(sorted_list: List[int], target: int) -> Optional[int]:
    """O(log n) - return index of target in sorted_list or None if missing."""
    lo, hi = 0, len(sorted_list) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_list[mid] == target:
            return mid
        if sorted_list[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


def merge_sort(seq: Iterable[int]) -> List[int]:
    """O(n log n) - stable merge sort returning a new sorted list."""
    arr = list(seq)
    if len(arr) <= 1:
        return arr

    def merge(a: List[int], b: List[int]) -> List[int]:
        i = j = 0
        out: List[int] = []
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                out.append(a[i]); i += 1
            else:
                out.append(b[j]); j += 1
        out.extend(a[i:])
        out.extend(b[j:])
        return out

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def factorial_recursive(n: int) -> int:
    """Recursive factorial. Beware recursion depth for large n."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci_generator() -> Generator[int, None, None]:
    """Yield an infinite Fibonacci sequence (0, 1, 1, 2, ...)."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


async def async_wait_and_square(x: int, delay: float = 0.01) -> int:
    """Small async example: wait then return x*x."""
    await asyncio.sleep(delay)
    return x * x


def test() -> None:
    """A small test function to exercise simple operations."""
    a = constant_time(1)
    b = constant_time(2)
    c = constant_time(3)

    i = 0
    s = 0
    while i < 10:
        d = a + b + c
        s += d
        i += 1
    # keep s so linters don't consider it unused
    print("loop sum:", s)


if __name__ == "__main__":
    print("constant_time(7)", constant_time(7))
    print("linear_sum(range(5))", linear_sum(range(5)))
    print("first 5 fibonacci numbers:", [next(fibonacci_generator()) for _ in range(5)])
    print("binary_search([1,2,3,4,5], 3) ->", binary_search([1,2,3,4,5], 3))
    print("merge_sort([5,3,6,2,1]) ->", merge_sort([5,3,6,2,1]))
    print("factorial_recursive(6)", factorial_recursive(6))
    print("len(quadratic_pair_sums([1,2,3])) ->", len(quadratic_pair_sums([1,2,3])))

    # tiny async demo
    try:
        loop = asyncio.get_event_loop()
        res = loop.run_until_complete(async_wait_and_square(4))
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        res = loop.run_until_complete(async_wait_and_square(4))
        loop.close()
    print("async_wait_and_square(4) ->", res)


