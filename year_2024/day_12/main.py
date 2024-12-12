DEBUG_PROBLEM = 1
from pprint import pprint


def open_input() -> list[str]:
    filepath = "input.txt"
    if DEBUG_PROBLEM in [1, 2]:
        print("DEBUG MODE ON")
        filepath = "input_sample.txt"

    with open(filepath, "r", encoding="utf-8") as f:
        return [list(line) for line in f.read().split("\n") if line]


def get_adjacent(x: int, y: int, n: int, m: int) -> list:
    adjacents = []
    for i in [-1, 1]:
        if 0 <= x + i < n:
            adjacents.append((x + i, y))
        if 0 <= y + i < m:
            adjacents.append((x, y + i))
    return adjacents


def problem_1() -> int:
    explored = set()
    regions = {}
    garden_plots = open_input()

    def explore_garden(x: int, y: int) -> None:
        current_flower = garden_plots[x][y]
        adjacents = get_adjacent(x, y, len(garden_plots), len(garden_plots[0]))

        for adj_x, adj_y in adjacents:
            if (adj_x, adj_y) in explored:
                continue
            if garden_plots[adj_x][adj_y] != current_flower:
                continue
            explored.add((adj_x, adj_y))
            if current_flower not in regions:
                regions[current_flower] = []
            regions[current_flower] = regions[current_flower] + [(adj_x, adj_y)]

    for m, row in enumerate(garden_plots):
        for n, _ in enumerate(row):
            if (m, n) in explored:
                continue
            explored.add((m, n))
            explore_garden(m, n)

    sum_ = 0
    for rgs in regions.values():
        for region in rgs:
            borders = 0
            for plot in region:
                for i in [-1, 1]:
                    if (plot[0] + i, plot[1]) not in region:
                        borders += 1
                    if (plot[0], plot[1] + i) not in region:
                        borders += 1
            sum_ += borders * len(region)
    print(sum_)
    return 0


def problem_2() -> int:
    return 0


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
