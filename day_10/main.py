DEBUG = True

TILES_MAPPING = {
    "|": ((0, -1), (0, 1)),
    "-": ((-1, 0), (1, 0)),
    "L": ((0, -1), (1, 0)),
    "J": ((0, -1), (-1, 0)),
    "7": ((-1, 0), (0, 1)),
    "F": ((1, 0), (0, 1)),
    ".": ((0, 0), (0, 0)),
    "S": None,
}


from pprint import pprint


def open_input():    
    if DEBUG:
        print("DEBUG MODE ON")
        lines: list = [
            "-L|F7",
            "7S-7|",
            "L|7||",
            "-L-J|",
            "L|-JF",
        ]
        # lines: list = [
        #     "7-F7-",
        #     ".FJ|7",
        #     "SJLL7",
        #     "|F--J",
        #     "LJ.LJ",
        # ]
    else:
        with open("day_10/input.txt", 'r') as file:
            lines: list = file.read().split("\n")
            if lines[-1] == "":
                lines.pop(-1)

        if not lines:
            return []

    return lines


def map_parsing(lines: list[str]) -> list[list[str]]:
    maps = [[c for c in line] for line in lines]

    reversed_map =  [list(row) for row in zip(*maps)]

    return reversed_map


def locate_starting_point(map: list[list[str]]):
    for i, row in enumerate(map):
        for j, el in enumerate(row):
            if el == "S":
                return (i, j)
    raise Exception("No starting point found in the map")


class Node:
    def __init__(self, value, prev_node= None, next_node= None) -> None:
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node


def problem_1():

    lines = open_input()

    map = map_parsing(lines)
    
    tiles_mapping = TILES_MAPPING

    created_nodes = [[None for _ in range(len(map))] for _ in range(len(map[0]))]
    
    x_start, y_start = locate_starting_point(map)
    created_nodes[x_start][y_start] = Node("S")
    starting_node = created_nodes[x_start][y_start]

    x_current, y_current = x_start, y_start
    while created_nodes[x_start][y_start].prev_node is Node:

        for nb_shift_x, nb_shift_y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:

            nb_x = x_current + nb_shift_x
            nb_y = y_current + nb_shift_y 

            if 0 <= nb_x < len(map[0]) and 0 <= nb_y < len(map):
                nb_tile = map[nb_x][nb_y]

                nb_in = (nb_x + tiles_mapping[nb_tile][0][0] , nb_y + tiles_mapping[nb_tile][0][1])
                nb_out = (nb_x + tiles_mapping[nb_tile][1][0] , nb_y + tiles_mapping[nb_tile][1][1])

                if nb_in == (x_current, y_current) or nb_out == (x_current, y_current):

                    if created_nodes[x_current][y_current].next_node is None:
                        if created_nodes[nb_x][nb_y] is None:
                            created_nodes[nb_x][nb_y] = Node(nb_tile, prev_node=created_nodes[x_current][y_current])

                    else:
                        if created_nodes[x][nb_y] is None:
                            created_nodes[nb_x][nb_y] = Node(nb_tile)

                        created_nodes[nb_x][nb_y].prev_node = created_nodes[nb_x][nb_y]
                    
                    x_current, y_current = nb_x, nb_y

    return None


if __name__ == "__main__":
    print(problem_1())

    # choice = input("Choose which problem to print (1 or 2): ")
    
    # if choice == "1":
    #     print(problem_1())
    # elif choice == "2":
    #     print(problem_2())
    # else:
    #     print("Invalid choice. Please enter 1 or 2.")
