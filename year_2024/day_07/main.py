DEBUG_PROBLEM = None


def open_input() -> tuple:
    filepath = "input.txt"
    if DEBUG_PROBLEM in [1, 2]:
        print("DEBUG MODE ON")
        filepath = "input_sample.txt"

    equations = []
    with open(filepath, "r", encoding="utf-8") as f:
        while True:
            line = f.readline().replace("\n", "")
            if not line:
                return equations
            equations.append(parse_line(line))


def parse_line(line: str) -> tuple:
    result, items = line.split(": ")
    return (int(result), [int(n) for n in items.split(" ")])


def problem_1() -> int:
    def create_equations(current_results: list, items: list[int]):
        if not items:
            return current_results

        new_results = []
        item = items.pop(0)
        for result in current_results:
            new_results += [result * item, result + item]

        return create_equations(new_results, items)

    equations = open_input()
    total_calibration_result = 0
    for result, items in equations:
        for r in create_equations([items[0]], items[1:]):
            if r == result:
                total_calibration_result += result
                break
    return total_calibration_result


def problem_2() -> int:
    def create_equations(current_results: list, items: list[int]):
        if not items:
            return current_results

        new_results = []
        item = items.pop(0)
        for result in current_results:
            new_results += [result * item, result + item, int(str(result) + str(item))]

        return create_equations(new_results, items)

    equations = open_input()
    total_calibration_result = 0
    for result, items in equations:
        for r in create_equations([items[0]], items[1:]):
            if r == result:
                total_calibration_result += result
                break
    return total_calibration_result


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
