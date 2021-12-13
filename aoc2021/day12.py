from typing import Counter, Dict, List, Set

from aocd import lines


CaveSystem = Dict[str, Set[str]]


def parse(input: List[str] = lines):
    system: CaveSystem = {}
    for line in input:
        [x, y] = line.split("-")
        system[x] = system[x].union([y]) if x in system else set([y])
        system[y] = system[y].union([x]) if y in system else set([x])
    return system


def part1(system: CaveSystem = parse()):
    paths: List[List[str]] = [["start"]]
    result = 0
    while len(paths) > 0:
        new_paths: List[List[str]] = []
        for path in paths:
            for c in system[path[-1]]:
                if c == "start":
                    continue
                elif c == "end":
                    result += 1
                elif c.isupper() or "end" in c or c not in path:
                    new_paths.append(path + [c])
        paths = new_paths
    return result


def part2(system: CaveSystem = parse(), p: List[str] = ["start"]):
    result = 0
    for c in system[p[-1]]:
        if c == "start":
            continue
        elif c == "end":
            result += 1
        elif c.isupper() or c not in p or all(c <= 1 for c in Counter(c for c in p if c.islower()).values()):
            result += part2(system, p + [c])
    return result


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
