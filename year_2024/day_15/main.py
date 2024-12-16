DEBUG_PROBLEM = 1


def open_input() -> tuple:
    filepath = "input.txt"
    if DEBUG_PROBLEM in [1, 2]:
        print("DEBUG MODE ON")
        filepath = "input_sample.txt"

    matrix = []
    instructions = ""
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

            matrix.append(list(line))

        return matrix, instructions


def problem_1() -> int:
    matrix, instructions = open_input()
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
