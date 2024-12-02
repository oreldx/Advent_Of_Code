DEBUG = False


def open_input() -> list[list[int]]:
    if DEBUG:
        print("DEBUG MODE ON")
        return [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9],
        ]

    filepath = "input.txt"
    reports = []
    with open(filepath, "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                return reports

            reports.append(parse_line(line))


def parse_line(line: str) -> list[int]:
    line = line.replace("\n", "")
    elements = line.split(" ")
    return [int(e) for e in elements]


def problem_1() -> int:
    def check_report(report: list[int]) -> bool:
        variation_direction = 0
        for idx, n in enumerate(report):
            if idx == 0:
                continue
            new_variation = n - report[idx - 1]
            if 1 > abs(new_variation) or abs(new_variation) > 3:
                return False

            if variation_direction == 0:
                variation_direction = new_variation
            # Variation changed direction
            if variation_direction * new_variation < 0:
                return False

        return True

    return sum(check_report(report) for report in open_input())


def problem_2() -> int:
    def check_report(
        report: list[int], direction: int = 0, damped: bool = False
    ) -> bool:
        if len(report) < 2:
            return True

        e1 = report[0]
        e2 = report[1]
        variation = e2 - e1
        if 1 > abs(variation) or abs(variation) > 3:
            if damped:
                return False
            return check_report(report[:1] + report[1 + 1 :], direction, True)

        if direction == 0:
            direction = variation / abs(variation)
        # Variation changed direction
        if direction * variation < 0:
            if damped:
                return False
            return check_report(report[:1] + report[1 + 1 :], direction, True)

        return check_report(report[1:], direction, damped)

    return sum(check_report(report) for report in open_input())


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
