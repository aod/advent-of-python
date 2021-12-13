from typing import List, Set, Tuple, cast
from dataclasses import dataclass

from aocd import data


XY = Tuple[int, int]


@dataclass
class Paper():
    dots: Set[XY]
    max_x: int
    max_y: int

    def fold(self, axis: int, n: int) -> 'Paper':
        dots: Set[XY] = set()
        for dot in self.dots:
            if dot[axis] < n:
                dots.add(dot)
            else:
                x, y = dot
                if axis == 1:
                    dots.add((x, self.max_y - y))
                else:
                    dots.add((self.max_x - x, y))

        max_x = self.max_x - n-1 if axis == 0 else self.max_x
        max_y = self.max_y - n-1 if axis == 1 else self.max_y

        return Paper(dots, max_x, max_y)

    def dump(self):
        for y in range(self.max_y+1):
            for x in range(self.max_x+1):
                print("█" if (x, y) in self.dots else ".", end="")
            print()
        print()


def parse(input: str = data) -> Tuple[Paper, List[Tuple[int, int]]]:
    split = input.split("\n\n")

    dots: Set[XY] = set()
    for line in split[0].splitlines():
        dots.add(cast(XY, tuple(int(x) for x in line.split(","))))

    folds: List[Tuple[int, int]] = []
    for fold in split[1].splitlines():
        axis, n = fold.split(" ")[2].split("=")
        folds.append((0 if axis == "x" else 1, int(n)))

    return (Paper(dots, max(x for x, _ in dots), max(y for _, y in dots)), folds)


def part1(input: str = data):
    paper, folds = parse(input)
    paper = paper.fold(*folds[0])
    return len(paper.dots)


def part2(input: str = data):
    paper, folds = parse(input)
    for axis, n in folds:
        paper = paper.fold(axis, n)
    paper.dump()


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print("Part 2:")
    part2()
