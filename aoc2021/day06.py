from typing import Dict
from aocd import data


def simulate(fishies: Dict[int, int], days: int):
    for _ in range(days):
        new_fishies: Dict[int, int] = {k: 0 for k in range(0, 9)}
        new_fishies[0] = fishies[1]
        new_fishies[1] = fishies[2]
        new_fishies[2] = fishies[3]
        new_fishies[3] = fishies[4]
        new_fishies[4] = fishies[5]
        new_fishies[5] = fishies[6]
        new_fishies[6] = fishies[0] + fishies[7]
        new_fishies[7] = fishies[8]
        new_fishies[8] = fishies[0]
        fishies = new_fishies
    return sum(fishies.values())


if __name__ == "__main__":
    initial = {k: 0 for k in range(9)}
    for x in data.split(","):
        initial[int(x)] += 1

    print(f"Part 1: {simulate(initial, 80)}")
    print(f"Part 2: {simulate(initial, 256)}")
