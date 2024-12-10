DEBUG_PROBLEM = 1


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


def problem_1() -> int:
    topographic_map = open_input()
    trails = []

    def get_adjacent(x: int, y: int) -> list:
        adjacent = []
        for i in [-1, 1]:
            if 0 <= x + i < len(topographic_map):

                adjacent.append((x + i, y))
            if 0 <= y + i < len(topographic_map[0]):
                adjacent.append((x, y + i))

        return [
            adj
            for adj in adjacent
            if topographic_map[adj[0]][adj[1]] == topographic_map[x][y] - 1
            or topographic_map[adj[0]][adj[1]] == topographic_map[x][y] + 1
            or topographic_map[adj[0]][adj[1]] == topographic_map[x][y]
        ]

    def explore_path(x: int, y: int, path: list):
        adjacents = get_adjacent(x, y)
        if not adjacents:
            return

        for adj in adjacents:
            if adj in path:
                continue
            if topographic_map[adj[0]][adj[1]] == 0:
                trails.append(path + [adj])
            explore_path(adj[0], adj[1], path + [adj])

    for m, col in enumerate(topographic_map):
        for n, cell in enumerate(col):
            print(n, m)
            if cell == 9:
                explore_path(m, n, [(m, n)])
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
