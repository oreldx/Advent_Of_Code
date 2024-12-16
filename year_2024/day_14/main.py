DEBUG_PROBLEM = None


def open_input() -> tuple:
    filepath = "input.txt"
    space_size = (101, 103)
    if DEBUG_PROBLEM in [1, 2]:
        print("DEBUG MODE ON")
        filepath = "input_sample.txt"
        space_size = (11, 7)

    robots = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f.read().split("\n"):
            if not line:
                continue

            position, velocity = line.split(" ")
            px, py = position.split("=")[-1].split(",")
            vx, vy = velocity.split("=")[-1].split(",")

            robot = {
                "p": (int(px), int(py)),
                "v": (int(vx), int(vy)),
            }

            robots.append(robot)

        return robots, space_size


def print_robot_on_space(robot: dict, space_size: tuple) -> None:
    for j in range(space_size[1]):
        for i in range(space_size[0]):
            if (i, j) == robot["p"]:
                print("1", end="")
            else:
                print(".", end="")
        print()


def problem_1() -> int:
    robots, space_size = open_input()
    seconds_elapsed = 100

    for _ in range(seconds_elapsed):
        for robot in robots:
            robot["p"] = (
                (robot["p"][0] + robot["v"][0]) % space_size[0],
                (robot["p"][1] + robot["v"][1]) % space_size[1],
            )

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for robot in robots:
        if robot["p"][0] < space_size[0] // 2 and robot["p"][1] < space_size[1] // 2:
            q1 += 1
        elif robot["p"][0] > space_size[0] // 2 and robot["p"][1] < space_size[1] // 2:
            q2 += 1
        elif robot["p"][0] < space_size[0] // 2 and robot["p"][1] > space_size[1] // 2:
            q3 += 1
        elif robot["p"][0] > space_size[0] // 2 and robot["p"][1] > space_size[1] // 2:
            q4 += 1

    return q1 * q2 * q3 * q4


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
