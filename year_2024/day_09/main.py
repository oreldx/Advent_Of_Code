DEBUG_PROBLEM = 2


def open_input() -> tuple:
    filepath = "input.txt"
    if DEBUG_PROBLEM in [1, 2]:
        print("DEBUG MODE ON")
        filepath = "input_sample.txt"

    disk = []
    with open(filepath, "r", encoding="utf-8") as f:
        while True:
            line = f.readline().replace("\n", "")
            if not line:
                return disk
            free_space = False
            file_idx = 0
            for c in line:
                for _ in range(int(c)):
                    if free_space:
                        disk.append(".")
                        continue
                    disk.append(file_idx)
                free_space = not free_space
                if not free_space:
                    file_idx += 1


def problem_1() -> int:
    storage = open_input()

    free_space_idx = 0
    for n_idx_reverse, n in enumerate(storage[::-1]):
        if n == ".":
            continue

        while free_space_idx < len(storage) and storage[free_space_idx] != ".":
            free_space_idx += 1

        n_idx = len(storage) - n_idx_reverse - 1
        if n_idx <= free_space_idx:
            break

        storage[free_space_idx] = n
        storage[n_idx] = "."

    return sum(idx * n for idx, n in enumerate(storage) if n != ".")


def problem_2() -> int:
    storage = open_input()

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
