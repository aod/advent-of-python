from aocd import lines


def part1():
    pos = [0, 0]
    for (cmd, delta) in [line.split(" ") for line in lines]:
        match cmd:
            case "forward": pos[0] += int(delta)
            case "down": pos[1] += int(delta)
            case "up": pos[1] -= int(delta)
    return pos[0] * pos[1]


def part2():
    pos = [0, 0]
    aim = 0
    for (cmd, delta) in [line.split(" ") for line in lines]:
        match cmd:
            case "down": aim += int(delta)
            case "up": aim -= int(delta)
            case "forward":
                pos[0] += int(delta)
                pos[1] += int(delta) * aim
    return pos[0] * pos[1]


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
