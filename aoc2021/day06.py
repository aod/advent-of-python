from typing import Dict
from aocd import data


def simulate(fishies: Dict[int, int], days: int):
    for _ in range(days):
        fishies = {
            0: fishies[1],
            1: fishies[2],
            2: fishies[3],
            3: fishies[4],
            4: fishies[5],
            5: fishies[6],
            6: fishies[0] + fishies[7],
            7: fishies[8],
            8: fishies[0],
        }
    return sum(fishies.values())


if __name__ == "__main__":
    initial = {k: 0 for k in range(9)}
    for x in data.split(","):
        initial[int(x)] += 1

    print(f"Part 1: {simulate(initial, 80)}")
    print(f"Part 2: {simulate(initial, 256)}")
