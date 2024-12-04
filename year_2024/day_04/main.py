DEBUG_PROBLEM = 1


def open_input() -> list[list[int]]:
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
