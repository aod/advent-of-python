from itertools import repeat
from collections import Counter
from typing import Callable, Generator, List, Tuple, cast
from aocd import data

XY = Tuple[int, int]
Vent = Tuple[XY, XY]
Vents = List[Vent]


def straight_lines(vent: Vent):
    (x1, y1), (x2, y2) = vent
    if x1 == x2:
        yield from zip(repeat(x1), range(min(y1, y2), max(y1, y2)+1))
    elif y1 == y2:
        yield from zip(range(min(x1, x2), max(x1, x2)+1), repeat(y1))


def all_lines(vent: Vent):
    (x1, y1), (x2, y2) = vent
    if x1 != x2 and y1 != y2:
        xs = range(x1, x2-1 if x1 > x2 else x2+1, -1 if x1 > x2 else 1)
        ys = range(y1, y2-1 if y1 > y2 else y2+1, -1 if y1 > y2 else 1)
        yield from zip(xs, ys)
    else:
        yield from straight_lines(vent)


def solve(lines: Vents, gen: Callable[[Vent], Generator[XY, None, None]]):
    floor = Counter([(coord, 1) for line in lines for coord in gen(line)])
    return sum(1 for coord in floor.values() if coord >= 2)


def parse(input: str) -> Vents:
    res: Vents = []
    for line in input.splitlines():
        s = line.split(" -> ")
        start: XY = cast(XY, tuple([int(x) for x in s[0].split(",")]))
        end: XY = cast(XY, tuple([int(x) for x in s[1].split(",")]))
        res.append((start, end))
    return res


if __name__ == "__main__":
    print(f"Part 1: {solve(parse(data), straight_lines)}")
    print(f"Part 2: {solve(parse(data), all_lines)}")
