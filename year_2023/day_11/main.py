DEBUG = False


def open_input() -> list[str]:    
    if DEBUG:
        print("DEBUG MODE ON")

        lines: list = [
            "...#......",
            ".......#..",
            "#.........",
            "..........",
            "......#...",
            ".#........",
            ".........#",
            "..........",
            ".......#..",
            "#...#.....",
        ]

    else:
        with open("input.txt", 'r') as file:
            lines: list = file.read().split("\n")
            if lines[-1] == "":
                lines.pop(-1)

        if not lines:
            return []

    return lines


def image_parser(data: list[str]) -> list[list[str]]:
    return [[c for c in line] for line in data]


def print_image(image: list[list[str]]) -> None:
    for row in image:
        line: str = ""
        for c in row:
            line += c
        print(line)


def expand_space(image: list[list[str]]) -> list[list[str]]:

    expansion_rows: list[int] = []
    for idx, row in enumerate(image):
        if row == ["." for _ in range(len(row))]:
            expansion_rows.append(idx)
    
    expansion_cols: list[int] = []
    for idx in range(len(image[0])):
        col = [image[i][idx] for i in range(len(image))]
        if col == ["." for _ in range(len(image))]:
            expansion_cols.append(idx)
    
    for idx in expansion_rows[::-1]:
        image = image[:idx] + [["." for _ in range(len(image[idx]))]] + image[idx:]

    for idx in expansion_cols[::-1]:
        for idx_row in range(len(image)):
            image[idx_row] = image[idx_row][:idx] + ["."] + image[idx_row][idx:]

    return image


def get_expanded_space(image: list[list[str]]) -> list[list[str]]:

    expansion_rows: list[int] = []
    for idx, row in enumerate(image):
        if row == ["." for _ in range(len(row))]:
            expansion_rows.append(idx)
    
    expansion_cols: list[int] = []
    for idx in range(len(image[0])):
        col = [image[i][idx] for i in range(len(image))]
        if col == ["." for _ in range(len(image))]:
            expansion_cols.append(idx)

    return {"row": expansion_rows, "col": expansion_cols}


def index_galaxies(image: list[list[str]]) -> tuple[list[list[str]], list[tuple[int, int]]]:
    idx: int = 1
    galaxies_position: list[tuple[int, int]] = []
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] == "#":
                image[i][j] = str(idx)
                galaxies_position.append((i, j))
                idx += 1
    return image, galaxies_position


def problem_1() -> int:

    data = open_input()

    image = image_parser(data)

    image = expand_space(image)

    image, galaxies_position = index_galaxies(image)

    sum_length: int = 0
    for i, current_galaxie_position in enumerate(galaxies_position[:-1]):
        for other_galaxie_position in galaxies_position[i+1:]:
            sum_length += sum([abs(current_galaxie_position[k]-other_galaxie_position[k]) for k in range(2)])

    return sum_length


def problem_2() -> int:

    data = open_input()

    image = image_parser(data)

    expanded_space_idx = get_expanded_space(image)

    image, galaxies_position = index_galaxies(image)

    sum_length: int = 0
    for i, current_galaxie_position in enumerate(galaxies_position[:-1]):
        for other_galaxie_position in galaxies_position[i+1:]:
            length: int = 0
            for idx, axe in enumerate(["row", "col"]):
                count_expanded_lines: int = 0
                for line_idx in expanded_space_idx[axe]:
                    if min(other_galaxie_position[idx], current_galaxie_position[idx]) < line_idx < max(other_galaxie_position[idx], current_galaxie_position[idx]):
                        count_expanded_lines += 1
                length += abs(current_galaxie_position[idx]-other_galaxie_position[idx]) + (1000000-min(1, count_expanded_lines)) * count_expanded_lines
            sum_length += length

    return sum_length


if __name__ == "__main__":
    choice = input("Choose which problem to print (1 or 2): ")
    
    if choice == "1":
        print(problem_1())
    elif choice == "2":
        print(problem_2())
    else:
        print("Invalid choice. Please enter 1 or 2.")
