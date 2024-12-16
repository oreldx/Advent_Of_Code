DEBUG_PROBLEM = None


def open_input(p_idx: int) -> list[str]:
    filepath = "input.txt"
    if DEBUG_PROBLEM in [1, 2]:
        print("DEBUG MODE ON")
        filepath = "input_sample.txt"

    situations = []
    with open(filepath, "r", encoding="utf-8") as f:
        situation = {}
        while True:
            line = f.readline()
            if not line:
                return situations
            line = line.replace("\n", "")
            if not line:
                continue
            if "A" in line:
                situation["A"] = [int(p.split("+")[-1]) for p in line.split(",")]
                continue
            if "B" in line:
                situation["B"] = [int(p.split("+")[-1]) for p in line.split(",")]
                continue
            situation["X"] = [
                int(p.split("=")[-1]) + 10000000000000 * (p_idx - 1)
                for p in line.split(",")
            ]
            situations.append(situation)
            situation = {}


def print_system(system: dict[str, dict[str, int]]) -> None:
    print(f"{system['A'][0]}x + {system['B'][0]}y = {system['X'][0]}")
    print(f"{system['A'][1]}x + {system['B'][1]}y = {system['X'][1]}")
    print()


def solve_system(system: dict[str, dict[str, int]]) -> tuple[float, float]:
    x1, y1, a1 = system["A"][0], system["B"][0], system["X"][0]
    x2, y2, a2 = system["A"][1], system["B"][1], system["X"][1]
    x = (y1 * a2 - y2 * a1) / (x2 * y1 - x1 * y2)
    y = (a1 - x1 * x) / y1
    return x, y


def problem(p_idx: int) -> int:
    situations = open_input(p_idx)

    tokens = 0
    for system in situations:
        x, y = solve_system(system)
        # If float, then it is not a solution
        if x % int(x) != 0 or y % int(y) != 0:
            continue
        tokens += int(x) * 3 + int(y)

    return tokens


def main() -> None:
    if DEBUG_PROBLEM in [1, 2]:
        print(problem(DEBUG_PROBLEM))
        return

    p_idx = input("Choose which problem to print (1 or 2): ")
    if p_idx in ["1", "2"]:
        print(problem(int(p_idx)))
        return
    print("Invalid choice. Please enter 1 or 2.")


main()
