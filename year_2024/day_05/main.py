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
    ordering_rules = {}
    order_lists = []
    for line in lines:
        if not line:
            continue

        if "," in line:
            order_lists.append([int(n) for n in line.split(",")])
            continue

        if "|" in line:
            a, b = line.split("|")
            if int(a) not in ordering_rules:
                ordering_rules[int(a)] = [int(b)]
                continue

            ordering_rules[int(a)].append(int(b))
    return ordering_rules, order_lists


def problem_1() -> int:
    ordering_rules, order_lists = open_input()
    valid_lists = []
    for order_list in order_lists:
        reversed_order_list = order_list[::-1]
        invalid = False
        for idx, n in enumerate(reversed_order_list):
            n_rules = ordering_rules.get(n, [])
            if any(m in reversed_order_list[idx:] for m in n_rules):
                invalid = True
                break
        if not invalid:
            valid_lists.append(order_list)
    return sum(order_list[len(order_list) // 2] for order_list in valid_lists)


def problem_2() -> int:

    def review_ordering_list(
        ordering_rules: dict, idx: int, order_list: list[int]
    ) -> list[int]:
        if idx == len(order_list) - 2:
            return order_list

        n = order_list[idx]
        for idx_m, m in enumerate(order_list[idx + 1 :]):
            if m in ordering_rules.get(n, []):
                new_order_list = order_list.copy()
                new_order_list[idx], new_order_list[idx_m + idx + 1] = (
                    new_order_list[idx_m + idx + 1],
                    new_order_list[idx],
                )
                return review_ordering_list(ordering_rules, idx, new_order_list)

        return review_ordering_list(ordering_rules, idx + 1, order_list)

    ordering_rules, order_lists = open_input()

    updated_lists = []
    for order_list in order_lists:
        reversed_order_list = order_list[::-1]
        invalid = False
        for idx, n in enumerate(reversed_order_list):
            n_rules = ordering_rules.get(n, [])
            if any(m in reversed_order_list[idx:] for m in n_rules):
                invalid = True
                break
        if invalid:
            updated_lists.append(
                review_ordering_list(ordering_rules, 0, reversed_order_list)
            )

    return sum(order_list[len(order_list) // 2] for order_list in updated_lists)


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
