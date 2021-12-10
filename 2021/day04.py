from typing import List, Set
from dataclasses import dataclass
from aocd import lines


@dataclass
class Board:
    board: List[List[int]]
    marked: Set[int]

    def unmarked(self):
        return set(cell for row in self.board for cell in row) - self.marked

    def has_won(self):
        for y, row in enumerate(self.board):
            if all(col in self.marked for col in row):
                return True
            if all(self.board[x][y] in self.marked for x in range(len(self.board[0]))):
                return True


def part1(draw, boards):
    bingo = [Board(b, set()) for b in boards]

    for num in draw:
        for board in bingo:
            board.marked.add(num)
            if board.has_won():
                return num * sum(board.unmarked())


def part2(draw, boards):
    bingo = [Board(b, set()) for b in boards]

    for num in draw:
        next_bingo = []
        for board in bingo:
            board.marked.add(num)
            if not board.has_won():
                next_bingo.append(board)
            elif len(bingo) == 1:
                return num * sum(board.unmarked())
        bingo = next_bingo


if __name__ == "__main__":
    draw = [int(x) for x in lines[0].split(",")]
    boards = [[int(x) for x in line.split(" ") if x]
              for line in lines[2:] if line]
    boards = [boards[i*5:i*5+5] for i in range(0, len(boards) // 5)]

    print(f"Part 1: {part1(draw, boards)}")
    print(f"Part 1: {part2(draw, boards)}")
