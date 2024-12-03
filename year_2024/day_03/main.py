DEBUG = True


def open_input() -> list[list[int]]:
    if DEBUG:
        print("DEBUG MODE ON")
        return [
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        ]

    filepath = "input.txt"
    expressions = []
    with open(filepath, "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                return expressions

            expressions.append(parse_line(line))


def parse_line(line: str) -> str:
    return line.replace("\n", "")


def problem_1() -> int:
    def expression_parser(expression: str) -> int:
        expression_pattern = "mul(d,d)"
        instructions = []
        current_mul = [""]
        pattern_cursor = 0
        for char in expression:
            print(current_mul)
            if expression_pattern[pattern_cursor] == "d":
                if char.isdigit():
                    if len(current_mul[-1]) < 3:
                        current_mul[-1] += char
                        continue

                if char == "," and 4 > len(current_mul[-1]) > 0:
                    current_mul.append("")
                    pattern_cursor += 1

            if expression_pattern[pattern_cursor] == char:
                print(expression_pattern[pattern_cursor], char)
                if pattern_cursor == ")":
                    instructions.append(current_mul)
                    current_mul = []
                    pattern_cursor = 0
                    continue
                pattern_cursor += 1
                continue

            current_mul = [""]
            pattern_cursor = 0
        print(instructions)

    expressions = open_input()
    for expression in expressions:
        print(expression)
        expression_parser(expression)
    return 0


def problem_2() -> int:

    return 0


def main() -> None:
    if DEBUG:
        print(problem_1())
        return

    match input("Choose which problem to print (1 or 2): "):
        case "1":
            print(problem_1())
        case "2":
            print(problem_2())
        case _:
            print("Invalid choice. Please enter 1 or 2.")


main()
