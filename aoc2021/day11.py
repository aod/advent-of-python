from typing import Dict, List, Set, Tuple
from itertools import count, product

from aocd import lines


SIZE = 10

XY = Tuple[int, int]
Octopuses = Dict[XY, int]


def parse(input: List[str] = lines) -> Octopuses:
    return {(x, y): int(input[y][x]) for x, y in product(range(SIZE), range(SIZE))}


def nbor_deltas(coord: XY):
    x, y = coord
    yield (x-1, y-1)
    yield (x, y-1)
    yield (x+1, y-1)

    yield (x-1, y)
    yield (x+1, y)

    yield (x-1, y+1)
    yield (x, y+1)
    yield (x+1, y+1)


def nbors(op: Octopuses, coord: XY):
    for nbor_coord in nbor_deltas(coord):
        if nbor_coord in op:
            yield (nbor_coord, op[nbor_coord])


def try_flash(op: Octopuses, coord: XY, flashes: Set[XY]):
    if op[coord] <= 9 or coord in flashes:
        return
    flashes.add(coord)
    for nbor_coord, _ in nbors(op, coord):
        op[nbor_coord] += 1
        try_flash(op, nbor_coord, flashes)


def simulate(op: Octopuses):
    for coord in product(range(SIZE), range(SIZE)):
        op[coord] += 1

    flashes: Set[XY] = set()
    for coord in product(range(SIZE), range(SIZE)):
        try_flash(op, coord, flashes)

    for flashed_coord in flashes:
        op[flashed_coord] = 0

    return len(flashes)


def part1(op: Octopuses = parse()):
    return sum(simulate(op) for _ in range(100))


def part2(op: Octopuses = parse()):
    for step in count(1):
        if simulate(op) == SIZE*SIZE:
            return step


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
