DEBUG_PROBLEM = None


def open_input() -> tuple:
    if DEBUG_PROBLEM in [1, 2]:
        print("DEBUG MODE ON")
        filepath = "input_sample.txt"
        with open(filepath, "r", encoding="utf-8") as f:
            input_sample = f.read()
            return parse_line_to_matrix(input_sample)
    filepath = "input.txt"
    with open(filepath, "r", encoding="utf-8") as f:
        input_sample = f.read()
        return parse_line_to_matrix(input_sample)


def parse_line_to_matrix(input_text: str) -> tuple:
    lines = input_text.split("\n")
    matrix = []
    start_pos = (0, 0)
    for line in lines:
        line = line.strip()
        if not line:
            break
        if "^" in line:
            start_pos = (line.index("^"), len(matrix))
        matrix.append(line)
    return matrix, start_pos


def problem_1() -> int:
    def rotate_guard(direction: str) -> str:
        directions = ["^", ">", "v", "<"]
        return directions[(directions.index(direction) + 1) % 4]

    def move_guard(matrix: list[str], pos: tuple, direction: str) -> tuple:
        x, y = pos
        match direction:
            case "^":
                y -= 1
            case "v":
                y += 1
            case "<":
                x -= 1
            case ">":
                x += 1
        if y < 0 or y > len(matrix) - 1 or x < 0 or x > len(matrix[0]) - 1:
            return pos, direction

        if matrix[y][x] == "#":
            return pos, rotate_guard(direction)
        return (x, y), direction

    matrix, current_pos = open_input()
    current_direction = "^"
    return_to_start = False
    positions = set()
    while not return_to_start:
        old_pos, old_direction = current_pos, current_direction
        current_pos, current_direction = move_guard(
            matrix, current_pos, current_direction
        )
        positions.add(current_pos)
        # guard didn't move or rotate because out of bounds
        if old_pos == current_pos and old_direction == current_direction:
            break

    return sum(1 for _ in positions)


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
