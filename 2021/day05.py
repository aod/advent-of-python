from math import copysign
from itertools import repeat
from collections import Counter
from typing import Callable, Generator, List, Tuple, cast
from aocd import data

XY = Tuple[int, int]
Vent = Tuple[XY, XY]


def straight_lines(vent: Vent):
    (x1, y1), (x2, y2) = vent
    if x1 == x2:
        yield from zip(repeat(x1), range(min(y1, y2), max(y1, y2)+1))
    elif y1 == y2:
        yield from zip(range(min(x1, x2), max(x1, x2)+1), repeat(y1))


def all_lines(vent: Vent):
    (x1, y1), (x2, y2) = vent
    if x1 != x2 and y1 != y2:
        xsgn = int(copysign(1, x2-x1))
        ysgn = int(copysign(1, y2-y1))
        yield from zip(range(x1, x2 + xsgn, xsgn), range(y1, y2 + ysgn, ysgn))
    else:
        yield from straight_lines(vent)


def solve(lines: List[Vent], gen: Callable[[Vent], Generator[XY, None, None]]):
    floor = Counter([(coord, 1) for line in lines for coord in gen(line)])
    return sum(1 for coord in floor.values() if coord >= 2)


def parse(input: str) -> List[Vent]:
    res: List[Vent] = []
    for line in input.splitlines():
        s = line.split(" -> ")
        start: XY = cast(XY, tuple([int(x) for x in s[0].split(",")]))
        end: XY = cast(XY, tuple([int(x) for x in s[1].split(",")]))
        res.append((start, end))
    return res


if __name__ == "__main__":
    print(f"Part 1: {solve(parse(data), straight_lines)}")
    print(f"Part 2: {solve(parse(data), all_lines)}")
