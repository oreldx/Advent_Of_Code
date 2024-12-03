DEBUG_PROBLEM = None


def open_input() -> list[list[int]]:
    if DEBUG_PROBLEM:
        print("DEBUG MODE ON")
        match DEBUG_PROBLEM:
            case 1:
                return [
                    "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
                ]
            case 2:
                return [
                    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
                ]
            case _:
                return []

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
    def expression_parser(expression: str) -> list:
        expression_pattern = "mul(d,d)"
        instructions = []
        current_mul = [""]
        pattern_cursor = 0
        for char in expression:
            if expression_pattern[pattern_cursor] == "d":
                # Number parsing
                if char.isdigit() and len(current_mul[-1]) < 3:
                    current_mul[-1] += char
                    continue

                # 1st number done
                if char == "," and 4 > len(current_mul[-1]) > 0:
                    current_mul.append("")
                    pattern_cursor += 1

                # 2nd number done
                if (
                    char == ")"
                    and len(current_mul) == 2
                    and 4 > len(current_mul[-1]) > 0
                ):
                    instructions.append(current_mul)
                    current_mul = [""]
                    pattern_cursor = 0
                    continue
            # Pattern matched
            if expression_pattern[pattern_cursor] == char:
                pattern_cursor += 1
                continue
            # Reset if pattern is not matched
            current_mul = [""]
            pattern_cursor = 0
        return instructions

    return sum(
        int(instruction[0]) * int(instruction[1])
        for expression in open_input()
        for instruction in expression_parser(expression)
    )


def problem_2() -> int:
    def sub_expression_activation_parser(
        sub_expression: str, current_activation: bool
    ) -> bool:
        enable_pos = sub_expression.rfind("do()")
        disable_pos = sub_expression.rfind("don't()")
        if enable_pos == -1 and disable_pos == -1:
            return current_activation
        return enable_pos > disable_pos

    def expression_parser(expression: str) -> list:
        expression_pattern = "mul(d,d)"
        instructions = []
        current_mul = [""]
        pattern_cursor = 0
        activation = True
        previous_pattern_matched_idx = 0
        for char_idx, char in enumerate(expression):

            if expression_pattern[pattern_cursor] == "d":
                # Number parsing
                if char.isdigit() and len(current_mul[-1]) < 3:
                    current_mul[-1] += char
                    continue

                # 1st number done
                if char == "," and 4 > len(current_mul[-1]) > 0:
                    current_mul.append("")
                    pattern_cursor += 1

                # 2nd number done
                if (
                    char == ")"
                    and len(current_mul) == 2
                    and 4 > len(current_mul[-1]) > 0
                ):
                    activation = sub_expression_activation_parser(
                        expression[previous_pattern_matched_idx:char_idx], activation
                    )
                    previous_pattern_matched_idx = char_idx
                    if activation:
                        instructions.append(current_mul)
                        current_mul = [""]
                        pattern_cursor = 0
                        continue
            # Pattern matched
            if expression_pattern[pattern_cursor] == char:
                pattern_cursor += 1
                continue
            # Reset if pattern is not matched
            current_mul = [""]
            pattern_cursor = 0
        return instructions

    return sum(
        int(instruction[0]) * int(instruction[1])
        for expression in open_input()
        for instruction in expression_parser(expression)
    )


def main() -> None:
    if DEBUG_PROBLEM:
        match DEBUG_PROBLEM:
            case 1:
                print(problem_1())
            case 2:
                print(problem_2())
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
