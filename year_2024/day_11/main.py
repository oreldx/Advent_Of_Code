from functools import cache

DEBUG_PROBLEM = None


def open_input() -> list[int]:
    filepath = "input.txt"
    if DEBUG_PROBLEM in [1, 2]:
        print("DEBUG MODE ON")
        filepath = "input_sample.txt"

    with open(filepath, "r", encoding="utf-8") as f:
        return [int(s) for s in f.readline().split(" ")]


def problem_1() -> int:
    blinking_times = 25
    stones = open_input()
    for _ in range(blinking_times):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                right_stone = str(stone)[len(str(stone)) // 2 :]
                left_stone = str(stone)[: len(str(stone)) // 2]

                new_stones += [int(left_stone), int(right_stone)]
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)


def problem_2() -> int:
    @cache
    def update_stone(stone: int, current_blink: int) -> list[int]:
        if current_blink == 75:
            return 1

        if stone == 0:
            return update_stone(1, current_blink + 1)

        if len(str(stone)) % 2 == 0:
            right_stone = str(stone)[len(str(stone)) // 2 :]
            left_stone = str(stone)[: len(str(stone)) // 2]
            return update_stone(int(left_stone), current_blink + 1) + update_stone(
                int(right_stone), current_blink + 1
            )

        return update_stone(stone * 2024, current_blink + 1)

    return sum(update_stone(stone, 0) for stone in open_input())


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
