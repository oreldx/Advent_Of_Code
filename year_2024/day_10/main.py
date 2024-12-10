DEBUG_PROBLEM = None


def open_input() -> str | list:
    filepath = "input.txt"
    if DEBUG_PROBLEM in [1, 2]:
        print("DEBUG MODE ON")
        filepath = "input_sample.txt"

    topographic_map = []
    with open(filepath, "r", encoding="utf-8") as f:
        while True:
            line = f.readline().replace("\n", "")
            if not line:
                return topographic_map
            if not topographic_map:
                topographic_map = [[int(c)] for c in line]
                continue
            for idx, c in enumerate(line):
                topographic_map[idx].append(int(c))


def get_adjacent(x: int, y: int, n: int, m: int) -> list:
    adjacents = []
    for i in [-1, 1]:
        if 0 <= x + i < n:
            adjacents.append((x + i, y))
        if 0 <= y + i < m:
            adjacents.append((x, y + i))
    return adjacents


def explore_path(x: int, y: int, path: list, topo_map: list, trails: list) -> None:
    n, m = len(topo_map), len(topo_map[0])
    for adj_x, adj_y in get_adjacent(x, y, n, m):
        if topo_map[adj_x][adj_y] != topo_map[x][y] - 1:  # Only go down by 1
            continue
        if (adj_x, adj_y) in path:  # Don't go back to the same cell
            continue
        if topo_map[adj_x][adj_y] == 0:  # Reach thes tart of the trail
            trails.append(path + [(adj_x, adj_y)])
        explore_path(adj_x, adj_y, path + [(adj_x, adj_y)], topo_map, trails)


def problem_1() -> int:
    trails = []
    highest_point = 9
    topographic_map = open_input()

    for m, col in enumerate(topographic_map):
        for n, cell in enumerate(col):
            if cell == highest_point:  # Start from the top
                explore_path(m, n, [(m, n)], topographic_map, trails)
    trailheads = {}
    for trail in trails:
        if trail[-1] not in trailheads:
            trailheads[trail[-1]] = set()
        trailheads[trail[-1]].add(trail[0])
    return sum(len(top) for top in trailheads.values())


def problem_2() -> int:
    trails = []
    highest_point = 9
    topographic_map = open_input()

    for m, col in enumerate(topographic_map):
        for n, cell in enumerate(col):
            if cell == highest_point:  # Top to bottom
                explore_path(m, n, [(m, n)], topographic_map, trails)
    return len(trails)


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
