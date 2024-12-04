DEBUG_PROBLEM = None


def open_input() -> list[list[str]]:
    if DEBUG_PROBLEM in [1, 2]:
        print("DEBUG MODE ON")
        matrix = []
        for line in [
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX",
        ]:
            matrix = parse_line_to_matrix(line, matrix)
        return matrix

    filepath = "input.txt"
    matrix = []
    with open(filepath, "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                return matrix
            matrix = parse_line_to_matrix(line, matrix)


def parse_line_to_matrix(line: str, matrix: list[list[str]]) -> list[list[str]]:
    line = line.replace("\n", "")
    if not matrix:
        return [[c] for c in line]

    for idx, c in enumerate(line):
        matrix[idx].append(c)
    return matrix


def problem_1() -> int:
    matrix = open_input()
    m = len(matrix)
    n = len(matrix[0])

    pattern = "XMAS"
    pattern_len = len(pattern)
    directions = [
        (0, -1),  # up
        (0, 1),  # down
        (-1, 0),  # left
        (1, 0),  # right
        (-1, -1),  # left-up
        (-1, 1),  # left-down
        (1, -1),  # right-up
        (1, 1),  # right-down
    ]

    strings = []
    for i, col in enumerate(matrix):
        for j, cell in enumerate(col):
            if cell != "X":
                continue
            strings += [
                "".join(matrix[i + k * di][j + k * dj] for k in range(pattern_len))
                for di, dj in directions
                if 0 <= i + (pattern_len - 1) * di < m
                and 0 <= j + (pattern_len - 1) * dj < n
            ]

    return sum(1 for s in strings if s == pattern)


def problem_2() -> int:
    matrix = open_input()
    pattern = "SAM"
    patterns = [pattern, pattern[::-1]]
    len_pattern = len(pattern)

    x_mas_count = 0
    for i, col in enumerate(matrix):
        x_clear = 1 <= i <= len(matrix) - 2
        if not x_clear:
            continue
        for j, cell in enumerate(col):
            if cell in ["X", "S", "M"]:
                continue
            y_clear = 1 <= j <= len(col) - 2
            if not y_clear:
                continue

            diags = [
                "".join(matrix[i - 1 + k][j + dj - dj * k] for k in range(len_pattern))
                for dj in [-1, 1]
            ]
            if all(diag in patterns for diag in diags):
                x_mas_count += 1
    return x_mas_count


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
