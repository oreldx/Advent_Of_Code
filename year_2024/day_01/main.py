from collections import Counter

DEBUG = False


def open_input() -> list[list[int]]:
    if DEBUG:
        print("DEBUG MODE ON")
        return [[3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]]

    filepath = "input.txt"
    lists = [[], []]
    with open(filepath, "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                return lists

            for idx, n in enumerate(parse_line(line)):
                lists[idx].append(n)


def parse_line(line: str) -> list[int]:
    line = line.replace("\n", "")
    elements = line.split("   ")
    return [int(e) for e in elements]


def problem_1() -> int:
    lists = open_input()

    sorted_lists = [sorted(l) for l in lists]

    return sum(abs(n2 - n1) for n1, n2 in zip(sorted_lists[0], sorted_lists[1]))


def problem_2() -> int:
    lists = open_input()

    occurences_hash = Counter(lists[1])

    return sum(n * occurences_hash.get(n, 0) for n in lists[0])


def main() -> None:
    if DEBUG:
        print(problem_2())
        return

    match input("Choose which problem to print (1 or 2): "):
        case "1":
            print(problem_1())
        case "2":
            print(problem_2())
        case _:
            print("Invalid choice. Please enter 1 or 2.")


main()
