from typing import List
from aocd import data


def gauss(n: int):
    return n * (n + 1) // 2


def part1(crabs: List[int]):
    return min([sum(abs(target - pos) for pos in crabs) for target in crabs])


def part2(crabs: List[int]):
    return min([sum(gauss(abs(target - pos)) for pos in crabs) for target in range(min(crabs), max(crabs))])


if __name__ == "__main__":
    data = [int(x) for x in data.split(",")]

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
