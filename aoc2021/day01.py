from typing import List
from aocd import numbers


def window(arr: List[int], n: int):
    return (arr[i:i + n] for i in range(len(arr) - n + 1))


def changes(measurements: List[int]):
    return (curr - prev for [prev, curr] in window(measurements, 2))


def larger_count(measurements: List[int]):
    return sum(1 if diff > 0 else 0 for diff in changes(measurements))


def solve(window_size: int):
    return larger_count([sum(xs) for xs in window(numbers, window_size)])


if __name__ == "__main__":
    print(f"Part 1: {solve(1)}")
    print(f"Part 2: {solve(3)}")
