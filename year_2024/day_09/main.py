DEBUG_PROBLEM = None


def open_input(problem_idx) -> str | list:
    filepath = "input.txt"
    if DEBUG_PROBLEM in [1, 2]:
        print("DEBUG MODE ON")
        filepath = "input_sample.txt"

    disk = []
    with open(filepath, "r", encoding="utf-8") as f:
        if problem_idx == 1:
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
        if problem_idx == 2:
            while True:
                line = f.readline().replace("\n", "")
                if not line:
                    return disk
                free_space = False
                file_idx = 0
                for c in line:
                    file_list = []
                    for _ in range(int(c)):
                        if free_space:
                            file_list.append(".")
                            continue
                        file_list.append(str(file_idx))
                    disk.append(file_list)
                    free_space = not free_space
                    if not free_space:
                        file_idx += 1
    return None


def problem_1() -> int:
    # HOW does this even work with the 2 digigts file issue
    storage = open_input(1)
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
    def add_first_enough_space(storage: list, n_file: str, curs: int) -> bool:
        for idx, s in enumerate(storage[:curs]):
            if "." in s and len(s) >= len(n_file):
                storage[idx] = n_file
                storage[curs] = ["." for _ in range(len(n_file))]
                left_space = len(s) - len(n_file)
                if left_space > 0:
                    storage.insert(idx + 1, ["." for _ in range(left_space)])
                return True
        return False

    storage = open_input(2)

    curs = len(storage) - 1
    while curs >= 0:
        n_file = storage[curs]
        if "." in n_file:
            curs -= 1
            continue
        if add_first_enough_space(storage, n_file, curs):
            continue
        curs -= 1

    global_idx = 0
    check_sum = 0
    for s in storage:
        for n in s:
            if n != ".":
                check_sum += global_idx * int(n)
            global_idx += 1
    return check_sum


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
