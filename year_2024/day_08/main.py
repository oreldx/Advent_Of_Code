DEBUG_PROBLEM = None


def open_input() -> tuple:
    filepath = "input.txt"
    if DEBUG_PROBLEM in [1, 2]:
        print("DEBUG MODE ON")
        filepath = "input_sample.txt"

    antennas = {}
    with open(filepath, "r", encoding="utf-8") as f:
        y = 0
        len_row = 0
        while True:
            line = f.readline().replace("\n", "")
            if not line:
                return antennas, (len_row, y)
            if len_row == 0:
                len_row = len(line)

            for x, c in enumerate(line):
                if c == ".":
                    continue
                if c not in antennas:
                    antennas[c] = [(x, y)]
                    continue
                antennas[c].append((x, y))
            y += 1


def problem_1() -> int:
    antennas, map_size = open_input()

    antinodes = set()
    for positions in antennas.values():
        for idx, (x_ref_pos, y_ref_pos) in enumerate(positions):
            for x_pos, y_pos in positions[:idx] + positions[idx + 1 :]:
                frequency = (
                    x_pos - x_ref_pos,
                    y_pos - y_ref_pos,
                )
                x_antinode, y_antinode = (
                    x_pos + frequency[0],
                    y_pos + frequency[1],
                )
                if 0 <= x_antinode < map_size[0] and 0 <= y_antinode < map_size[1]:
                    antinodes.add((x_antinode, y_antinode))
    return len(antinodes)


def problem_2() -> int:
    antennas, (n, m) = open_input()

    antinodes = set()
    for positions in antennas.values():
        for idx, (x_ref_pos, y_ref_pos) in enumerate(positions):
            for x_pos, y_pos in positions[:idx] + positions[idx + 1 :]:
                x_freq, y_freq = (
                    x_pos - x_ref_pos,
                    y_pos - y_ref_pos,
                )
                modulo = 1
                while True:
                    x_antinode, y_antinode = (
                        x_pos + x_freq * modulo,
                        y_pos + y_freq * modulo,
                    )
                    if (
                        0 > x_antinode
                        or x_antinode >= n
                        or 0 > y_antinode
                        or y_antinode >= m
                    ):
                        break
                    antinodes.add((x_antinode, y_antinode))
                    modulo += 1

            if len(positions) == 1:
                continue

            antinodes.add((x_ref_pos, y_ref_pos))

    return len(antinodes)


def print_antinodes_map(antinodes: set, map_size: tuple) -> None:
    for y in range(map_size[1]):
        for x in range(map_size[0]):
            if (x, y) not in antinodes:
                print(".", end="")
            else:
                print("#", end="")
        print()


def main() -> None:
    if DEBUG_PROBLEM:
        match DEBUG_PROBLEM:
            case 1:
                print(problem_1())
                return
            case 2:
                print(problem_2())
                return
            case _:
                return

    match input("Choose which problem to print (1 or 2): "):
        case "1":
            print(problem_1())
        case "2":
            print(problem_2())
        case _:
            print("Invalid choice. Please enter 1 or 2.")


main()
