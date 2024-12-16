import operator
import functools

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


def print_robots_on_space(robots: list[dict], space_size: tuple) -> None:
    robots_positions = [robot["p"] for robot in robots]
    for j in range(space_size[1]):
        for i in range(space_size[0]):
            if (i, j) in robots_positions:
                print("#", end="")
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

    qs = [0 for _ in range(4)]
    half_x, half_y = space_size[0] // 2, space_size[1] // 2
    for robot in robots:
        if robot["p"][0] < half_x and robot["p"][1] < half_y:
            qs[0] += 1
        elif robot["p"][0] > half_x and robot["p"][1] < half_y:
            qs[1] += 1
        elif robot["p"][0] < half_x and robot["p"][1] > half_y:
            qs[2] += 1
        elif robot["p"][0] > half_x and robot["p"][1] > half_y:
            qs[3] += 1

    return functools.reduce(operator.mul, qs)


def problem_2() -> int:
    robots, space_size = open_input()
    seconds_elapsed = 10000
    frame_entropies = []
    for _ in range(seconds_elapsed):
        lines = [["." for _ in range(space_size[0])] for _ in range(space_size[1])]
        for robot in robots:
            robot["p"] = (
                (robot["p"][0] + robot["v"][0]) % space_size[0],
                (robot["p"][1] + robot["v"][1]) % space_size[1],
            )
            lines[robot["p"][1]][robot["p"][0]] = "#"
        frame_entropies.append(sum(1 for line in lines if "#" * 7 in "".join(line)))
    return frame_entropies.index(max(frame_entropies))


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
