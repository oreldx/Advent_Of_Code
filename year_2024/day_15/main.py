DEBUG_PROBLEM = 2
DIRECTIONS = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}


def open_input() -> tuple:
    filepath = "input.txt"
    if DEBUG_PROBLEM in [1, 2]:
        print("DEBUG MODE ON")
        filepath = f"input_sample_{DEBUG_PROBLEM}.txt"

    matrix = []
    instructions = ""
    robot = (None, None)
    half_part = False
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f.read().split("\n"):
            if not line:
                if half_part:
                    break
                half_part = True
                continue

            if half_part:
                instructions += line
                continue

            if robot == (None, None) and "@" in line:
                robot = (line.index("@"), len(matrix))
            matrix.append(list(line))

        return matrix, instructions, robot


def print_matrix(matrix: list[list]) -> None:
    for row in matrix:
        print("".join(row))


def attempt_move_robot(robot: tuple, direction: tuple, matrix: list[list]) -> tuple:
    adj_x, adj_y = (
        robot[0] + DIRECTIONS[direction][0],
        robot[1] + DIRECTIONS[direction][1],
    )
    if matrix[adj_y][adj_x] == ".":
        return adj_x, adj_y
    return robot


def problem_1() -> int:
    matrix, instructions, robot = open_input()
    for instruction in instructions:
        robot_moved = attempt_move_robot(robot, instruction, matrix)
        if robot_moved != robot:
            matrix[robot[1]][robot[0]] = "."
            matrix[robot_moved[1]][robot_moved[0]] = "@"
            robot = robot_moved
            continue

        curs = robot
        while matrix[curs[1]][curs[0]] not in ["#", "."]:
            curs = (
                curs[0] + DIRECTIONS[instruction][0],
                curs[1] + DIRECTIONS[instruction][1],
            )
        if matrix[curs[1]][curs[0]] == "#":
            continue

        while curs != robot:
            matrix[curs[1]][curs[0]] = matrix[curs[1] - DIRECTIONS[instruction][1]][
                curs[0] - DIRECTIONS[instruction][0]
            ]
            curs = (
                curs[0] - DIRECTIONS[instruction][0],
                curs[1] - DIRECTIONS[instruction][1],
            )

        matrix[robot[1]][robot[0]] = "."
        robot = (
            robot[0] + DIRECTIONS[instruction][0],
            robot[1] + DIRECTIONS[instruction][1],
        )

    sum_ = 0
    for j, col in enumerate(matrix):
        for i, cell in enumerate(col):
            if cell == "O":
                sum_ += (j) * 100 + (i)

    return sum(
        (j) * 100 + (i)
        for j, col in enumerate(matrix)
        for i, cell in enumerate(col)
        if cell == "O"
    )


def problem_2() -> int:
    def scale_map(matrix: list[list]) -> list[list]:
        new_matrix = []
        for row in matrix:
            new_row = []
            for cell in row:
                print(cell)
                match cell:
                    case "#":
                        new_row += ["#", "#"]
                    case "@":
                        new_row += ["@", "."]
                    case ".":
                        new_row += [".", "."]
                    case "O":
                        new_row += ["[", "]"]
                    case _:
                        raise ValueError("Invalid cell value")
            new_matrix.append(new_row)
        return new_matrix

    def check_box(x: int, y: int, direction: tuple) -> False:
        if matrix[y][x] == "[":
            return check_box(x + 1, y, direction) and check_box(
                x + direction[0], y + direction[1], direction
            )
        if matrix[y][x] == "]":
            return check_box(x - 1, y, direction) and check_box(
                x + direction[0], y + direction[1], direction
            )
        return False

    def shift_boxes(x: int, y: int, direction: tuple) -> list[list]:
        if matrix[y][x] == "[":
            matrix = shift_boxes(x + 1, y, direction)
            matrix = shift_boxes(x + direction[0], y + direction[1], direction)
        if matrix[y][x] == "]":
            matrix = shift_boxes(x - 1, y, direction)
            matrix = shift_boxes(x + direction[0], y + direction[1], direction)
        matrix[y + direction[1]][x + direction[0]] = matrix[y][x]
        matrix[y][x] = "."
        return matrix

    matrix, instructions, robot = open_input()
    matrix = scale_map(matrix)
    for instruction in instructions:
        robot_moved = attempt_move_robot(robot, instruction, matrix)
        if robot_moved != robot:
            matrix[robot[1]][robot[0]] = "."
            matrix[robot_moved[1]][robot_moved[0]] = "@"
            robot = robot_moved
            continue

        # Horizontal box shift same as p1
        if instruction in ["<", ">"]:
            curs = robot
            while matrix[curs[1]][curs[0]] not in ["#", "."]:
                curs = (
                    curs[0] + DIRECTIONS[instruction][0],
                    curs[1] + DIRECTIONS[instruction][1],
                )

            # Robot stuck
            if matrix[curs[1]][curs[0]] == "#":
                continue

            while curs != robot:
                matrix[curs[1]][curs[0]] = matrix[curs[1] - DIRECTIONS[instruction][1]][
                    curs[0] - DIRECTIONS[instruction][0]
                ]
                curs = (
                    curs[0] - DIRECTIONS[instruction][0],
                    curs[1] - DIRECTIONS[instruction][1],
                )

        # Vertical box shift requires recursive check
        if instruction in ["^", "v"]:
            # Robot stuck
            if not check_box(
                robot[0] + DIRECTIONS[instruction][0],
                robot[1] + DIRECTIONS[instruction][1],
                DIRECTIONS[instruction],
            ):
                continue

            matrix = shift_boxes(
                robot[0] + DIRECTIONS[instruction][0],
                robot[1] + DIRECTIONS[instruction][1],
                DIRECTIONS[instruction],
            )

        matrix[robot[1]][robot[0]] = "."
        robot = (
            robot[0] + DIRECTIONS[instruction][0],
            robot[1] + DIRECTIONS[instruction][1],
        )

    sum_ = 0
    for j, col in enumerate(matrix):
        for i, cell in enumerate(col):
            if cell == "O":
                sum_ += (j) * 100 + (i)

    return sum(
        (j) * 100 + (i)
        for j, col in enumerate(matrix)
        for i, cell in enumerate(col)
        if cell == "O"
    )

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
