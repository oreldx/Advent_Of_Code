DEBUG = False


def open_input():    
    if DEBUG:
        print("DEBUG MODE ON")
        lines: list = [
            "0 3 6 9 12 15",
            "1 3 6 10 15 21",
            "10 13 16 21 30 45",
        ]
    else:
        with open("day_9/input.txt", 'r') as file:
            lines: list = file.read().split("\n")
            if lines[-1] == "":
                lines.pop(-1)

        if not lines:
            return []

    return lines


def line_parser(line_string: str) -> list:
    return [int(num) for num in line_string.split(" ")]


def stack_builder(line: str) -> list[list[int]]:
    
    values: list[list[int]] = [line_parser(line)]

    while not all(value == 0 for value in values[-1]):
        prev_line = values[-1]
        values.append([])

        for i in range(len(prev_line) - 1):
            values[-1].append(prev_line[i+1]-prev_line[i])

    return values


def problem_1():
    
    lines: list = open_input()
    
    total = 0
    for line in lines:
        values: list[list[int]] = stack_builder(line)

        prediction = 0
        for i in range(len(values)-1, -1, -1):
            prediction += values[i][-1]

        total += prediction

    return total


def problem_2():
    
    lines: list = open_input()
    
    total = 0
    for line in lines:

        values: list[list[int]] = stack_builder(line)

        prediction = 0
        for i in range(len(values)-1, -1, -1):
            prediction = values[i][0] - prediction

        total += prediction

    return total


if __name__ == "__main__":
    choice = input("Choose which problem to print (1 or 2): ")
    
    if choice == "1":
        print(problem_1())
    elif choice == "2":
        print(problem_2())
    else:
        print("Invalid choice. Please enter 1 or 2.")
