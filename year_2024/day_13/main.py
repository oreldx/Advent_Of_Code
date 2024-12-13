DEBUG_PROBLEM = 1


def open_input() -> list[str]:
    filepath = "input.txt"
    if DEBUG_PROBLEM in [1, 2]:
        print("DEBUG MODE ON")
        filepath = "input_sample.txt"

    situation = []
    with open(filepath, "r", encoding="utf-8") as f:
        situation = {}
        while True:
            line = f.readline().replace("\n", "")
            if not line:
                break
            line = f.read()
            if "A" in line:
                px, py = line.split(",")
                situation["A"] = {
                    "x": int(px.split("+")[-1]),
                    "y": int(py.split("+")[-1]),
                }
                continue
            if "B" in line:
                px, py = line.split(",")
                situation["B"] = {
                    "x": int(px.split("+")[-1]),
                    "y": int(py.split("+")[-1]),
                }
                continue
            px, py = line.split(",")
            situation["X"] = {
                "x": int(px.split("=")[-1]),
                "y": int(py.split("=")[-1]),
            }


def problem_1() -> int:
    print(open_input())
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
