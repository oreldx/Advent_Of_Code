DEBUG_PROBLEM = 2


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
    region_types = {}
    garden_plots = open_input()

    def explore_garden(x: int, y: int) -> None:
        current_flower = garden_plots[x][y]
        adjacents = get_adjacent(x, y, len(garden_plots), len(garden_plots[0]))
        tmp = [(x, y)]
        for adj_x, adj_y in adjacents:
            if (adj_x, adj_y) in explored:
                continue
            if garden_plots[adj_x][adj_y] != current_flower:
                continue
            explored.add((adj_x, adj_y))
            tmp += explore_garden(adj_x, adj_y)
        return tmp

    for m, row in enumerate(garden_plots):
        for n, plant in enumerate(row):
            if (m, n) in explored:
                continue
            explored.add((m, n))
            region_types.setdefault(plant, []).append(explore_garden(m, n))
    cost = 0
    for regions in region_types.values():
        for region in regions:
            borders = 0
            for plot in region:
                for i in [-1, 1]:
                    if (plot[0] + i, plot[1]) not in region:
                        borders += 1
                    if (plot[0], plot[1] + i) not in region:
                        borders += 1
            cost += borders * len(region)
    return cost


def problem_2() -> int:
    explored = set()
    region_types = {}
    garden_plots = open_input()

    def explore_garden(x: int, y: int) -> None:
        current_flower = garden_plots[x][y]
        adjacents = get_adjacent(x, y, len(garden_plots), len(garden_plots[0]))
        tmp = [(x, y)]
        for adj_x, adj_y in adjacents:
            if (adj_x, adj_y) in explored:
                continue
            if garden_plots[adj_x][adj_y] != current_flower:
                continue
            explored.add((adj_x, adj_y))
            tmp += explore_garden(adj_x, adj_y)
        return tmp

    for m, row in enumerate(garden_plots):
        for n, plant in enumerate(row):
            if (m, n) in explored:
                continue
            explored.add((m, n))
            region_types.setdefault(plant, []).append(explore_garden(m, n))

    cost = 0
    for plant, regions in region_types.items():
        for region in regions:
            corners = 0
            # TODO
            # 1. Find the edges of the region
            # 2. Find the corners of the region
            #   - Outside cornes: if 2 consecutive edges are not in the region
            #   - Inner corners: if 2 consecutive edges are in the region
            cost += corners * len(region)

    return cost


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
