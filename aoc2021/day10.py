from typing import List

from aocd import lines


opposites = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

part1_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def part1(subsystem: List[str] = lines):
    score = 0
    for line in subsystem:
        stack: List[str] = []
        for char in line:
            match char:
                case '(' | '[' | '{' | '<':
                    stack.append(char)
                case _:
                    if opposites[stack.pop()] != char:
                        score += part1_scores[char]
                        break
    return score


part2_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def part2(subsystem: List[str] = lines):
    incomplete: List[List[str]] = []
    for line in subsystem:
        stack: List[str] = []
        is_legal = True
        for char in line:
            match char:
                case '(' | '[' | '{' | '<':
                    stack.append(char)
                case _:
                    if opposites[stack.pop()] != char:
                        is_legal = False
                        break
        if is_legal and len(stack) > 0:
            incomplete.append(stack)

    result: List[int] = []
    for stack in incomplete:
        stack.reverse()
        score = 0
        for char in stack:
            score = score * 5 + part2_scores[opposites[char]]
        result.append(score)

    result.sort()
    return result[len(result) // 2]


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
