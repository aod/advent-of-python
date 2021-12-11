import sys
from typing import List
from aocd import data


def part1(crabs: List[int]):
    min_fuel = sys.maxsize
    for target in crabs:
        fuel = 0
        for pos in crabs:
            fuel += abs(target - pos)
        if fuel < min_fuel:
            min_fuel = fuel
    return min_fuel


def part2(crabs: List[int]):
    min_fuel = sys.maxsize
    for target in range(min(crabs), max(crabs)):
        fuel = 0
        for pos in crabs:
            n = abs(target - pos)
            fuel += n * (n + 1) // 2
        if fuel < min_fuel:
            min_fuel = fuel
    return min_fuel


if __name__ == "__main__":
    data = [int(x) for x in data.split(",")]

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
