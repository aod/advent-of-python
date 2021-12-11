from typing import List, Set
from aocd import lines


def part1(displays: List[str] = lines):
    result = 0
    for display in displays:
        _, output = tuple([part.split(" ") for part in display.split(" | ")])
        for digit in output:
            match len(digit):
                case 2: result += 1
                case 4: result += 1
                case 3: result += 1
                case 7: result += 1
    return result


def part2(displays: List[str]):
    result = 0

    for display in displays:
        patterns, output = tuple([part.split(" ")
                                  for part in display.split(" | ")])
        patterns.sort(key=len)

        stack = [set(x) for x in patterns]
        lut: List[Set[str]] = [set() for _ in range(10)]

        for pattern in stack:
            match len(pattern):
                case 2: lut[1] = pattern
                case 4: lut[4] = pattern
                case 3: lut[7] = pattern
                case 7: lut[8] = pattern
                case 5:
                    if len(pattern - lut[1]) == 3:
                        lut[3] = pattern
                    elif len(pattern - lut[4]) == 2:
                        lut[5] = pattern
                    else:
                        lut[2] = pattern
                case 6:
                    if len(pattern - lut[4]) == 2:
                        lut[9] = pattern
                    elif len(pattern - lut[1]) == 4:
                        lut[0] = pattern
                    else:
                        lut[6] = pattern

        output_value = 0
        for pattern in output:
            for digit_val, digit in enumerate(lut):
                if set(pattern) == digit:
                    output_value = output_value * 10 + digit_val
                    break
        result += output_value

    return result


if __name__ == "__main__":
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
