from typing import Dict, Generator, List, Tuple
from math import prod
from itertools import product

from aocd import data


XY = Tuple[int, int]
Heightmap = Dict[XY, Tuple[int, bool]]


def nbor_deltas(coord: XY) -> Generator[XY, None, None]:
    x, y = coord
    yield (x, y+1)
    yield (x+1, y)
    yield (x, y-1)
    yield (x-1, y)


def parse(input: str = data) -> Heightmap:
    hm: Heightmap = {}
    for y, line in enumerate(input.splitlines()):
        for x, cell in enumerate(line):
            hm[(x, y)] = (int(cell), False)
    return hm


def part1(hm: Heightmap = parse(), w: int = 100, h: int = 100):
    low_points: List[int] = []
    for coord in product(range(w), range(h)):
        height, _ = hm[coord]
        nbors_coords = (nbor for nbor in nbor_deltas(coord) if nbor in hm)
        nbors_cells = (hm[coord] for coord in nbors_coords)
        if all(nbor_height > height for nbor_height, _ in nbors_cells):
            low_points.append(height)
    return sum(height+1 for height in low_points)


def basin(hm: Heightmap, coord: XY) -> int:
    hm[coord] = (hm[coord][0], True)
    size = 0
    for nbor_coord in (nbor for nbor in nbor_deltas(coord) if nbor in hm):
        nbor_height, nbor_seen = hm[nbor_coord]
        if nbor_height != 9 and not nbor_seen:
            size += basin(hm, nbor_coord)
    return size + 1


def part2(hm: Heightmap = parse(), w: int = 100, h: int = 100):
    basins: List[int] = []
    for coord in product(range(w), range(h)):
        height, seen = hm[coord]
        if not seen and height != 9:
            basins.append(basin(hm, coord))
    basins.sort()
    return prod(basins[-3:])


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
