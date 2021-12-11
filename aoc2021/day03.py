from typing import Callable, List
from aocd import lines


def part1(bit_size: int = 12):
    numbers = [int(line, 2) for line in lines]
    gamma = 0
    epsilon = 0

    for i in range(bit_size):
        mcb = sum((num >> i) & 1 for num in numbers)
        if mcb >= len(numbers) // 2:
            gamma |= (1 << i)
        else:
            epsilon |= (1 << i)

    return gamma * epsilon


def common(numbers: List[int], nth_bit: int, bit_size: int = 12):
    mcbits: List[List[int]] = [[], []]
    for num in numbers:
        bit = (num >> (bit_size - 1 - nth_bit)) & 1
        mcbits[bit].append(num)
    return mcbits


def bit_criteria(numbers: List[int], criteria: Callable[[List[List[int]]], List[int]], bit_size: int = 12):
    numbers = list(numbers)

    for i in range(bit_size):
        if len(numbers) <= 1:
            break

        mcbits = common(numbers, i, bit_size)
        numbers = criteria(mcbits)

    return numbers[0]


def oxygen_criteria(mcbits: List[List[int]]):
    return mcbits[0] if len(mcbits[0]) > len(mcbits[1]) else mcbits[1]


def co2_criteria(mcbits: List[List[int]]):
    return mcbits[0] if len(mcbits[0]) <= len(mcbits[1]) else mcbits[1]


def part2(bit_size: int = 12):
    numbers = [int(line, 2) for line in lines]

    oxygen_rate = bit_criteria(numbers, oxygen_criteria, bit_size)
    co2_rate = bit_criteria(numbers, co2_criteria, bit_size)

    return oxygen_rate * co2_rate


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
