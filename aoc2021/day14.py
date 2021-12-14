from typing import Dict, List,  Tuple
from collections import OrderedDict

from aocd import lines


def parse(input: List[str] = lines) -> Tuple[OrderedDict[str, int], Dict[str, str]]:
    polymer: Dict[str, int] = OrderedDict()
    for x in zip(input[0][0:], input[0][1:]):
        k = "".join(list(x))
        if k in polymer:
            polymer[k] += 1
        else:
            polymer[k] = 1
    rules: Dict[str, str] = {}
    for line in input[2:]:
        split = line.split(" -> ")
        rules[split[0]] = split[1]
    return (polymer, rules)


def apply(polymer: OrderedDict[str, int], rules: Dict[str, str]):
    next: Dict[str, int] = OrderedDict()
    for pair in polymer:
        a = pair[0]+rules[pair]
        if a in next:
            next[a] += polymer[pair]
        else:
            next[a] = polymer[pair]
        b = rules[pair]+pair[1]
        if b in next:
            next[b] += polymer[pair]
        else:
            next[b] = polymer[pair]
    return next


def quantities(polymer: Dict[str, int]):
    result: Dict[str, int] = {next(iter(polymer))[0]: 1}
    for pair in polymer:
        k = pair[1]
        if k in result:
            result[k] += polymer[pair]
        else:
            result[k] = polymer[pair]
    return result


def solve(n: int):
    polymer, rules = parse()
    for _ in range(n):
        polymer = apply(polymer, rules)
    values = quantities(polymer).values()
    return max(values) - min(values)


if __name__ == "__main__":
    print(f"Part 1: {solve(10)}")
    print(f"Part 2: {solve(40)}")
