DEBUG = True

TILES_MAPPING = {
    "|": [(0, -1), (0, 1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
    ".": [(0, 0)],
    "S": [(-1, 0), (0, -1), (1, 0), (0, 1)],
}


def open_input():    
    if DEBUG:
        print("DEBUG MODE ON")

        # lines: list = [
        #     "-L|F7",
        #     "7S-7|",
        #     "L|7||",
        #     "-L-J|",
        #     "L|-JF",
        # ]
        # lines: list = [
        #     "7-F7-",
        #     ".FJ|7",
        #     "SJLL7",
        #     "|F--J",
        #     "LJ.LJ",
        # ]

        # lines: list = [
        #     "...........",
        #     ".S-------7.",
        #     ".|F-----7|.",
        #     ".||.....||.",
        #     ".||.....||.",
        #     ".|L-7.F-J|.",
        #     ".|..|.|..|.",
        #     ".L--J.L--J.",
        #     "...........",
        # ]

        # lines: list = [
        #     ".F----7F7F7F7F-7....",
        #     ".|F--7||||||||FJ....",
        #     ".||.FJ||||||||L7....",
        #     "FJL7L7LJLJ||LJ.L-7..",
        #     "L--J.L7...LJS7F-7L7.",
        #     "....F-J..F7FJ|L7L7L7",
        #     "....L7.F7||L7|.L7L7|",
        #     ".....|FJLJ|FJ|F7|.LJ",
        #     "....FJL-7.||.||||...",
        #     "....L---J.LJ.LJLJ...",
        # ]

        lines: list = [
            "FF7FSF7F7F7F7F7F---7",
            "L|LJ||||||||||||F--J",
            "FL-7LJLJ||||||LJL-77",
            "F--JF--7||LJLJ7F7FJ-",
            "L---JF-JLJ.||-FJLJJ7",
            "|F|F-JF---7F7-L7L|7|",
            "|FFJF7L7F-JF7|JL---7",
            "7-L-JL7||F7|L7F-7F7|",
            "L.L7LFJ|||||FJL7||LJ",
            "L7JLJL-JLJLJL--JLJ.L",
        ]
    else:
        with open("day_10/input.txt", 'r') as file:
            lines: list = file.read().split("\n")
            if lines[-1] == "":
                lines.pop(-1)

        if not lines:
            return []

    return lines


def map_parsing(lines: list[str]) -> list[list[str]]:
    map = []
    for idx_col in range(len(lines[0])):
        col = []
        for idx_row in range(len(lines)):
            col.append(lines[idx_row][idx_col])
        map.append(col)

    return map


def locate_starting_point(map: list[list[str]]):
    for i, col in enumerate(map):
        for j, el in enumerate(col):
            if el == "S":
                return (i, j)
    raise Exception("No starting point found in the map")


class Node:
    def __init__(self, value, prev = None, next = None) -> None:
        self.value = value
        self.prev = prev
        self.next = next


def loop_finder(starting_point: tuple[int, int], map: list[list[str]]) -> tuple[Node, list[list]]:
    tiles_mapping = TILES_MAPPING

    created_nodes = [[None for _ in range(len(map[0]))] for _ in range(len(map))]

    start_x, start_y = starting_point

    created_nodes[start_x][start_y] = Node("S")
    starting_node = created_nodes[start_x][start_y]

    current_x, current_y = start_x, start_y
    prev_x, prev_y = (-1, -1)

    while created_nodes[start_x][start_y].prev is None:
        
        current_node = created_nodes[current_x][current_y]

        for neighbour_shift_x, neighbour_shift_y in tiles_mapping[current_node.value]:
            neighbour_x = current_x + neighbour_shift_x
            neighbour_y = current_y + neighbour_shift_y 
            
            inside_map_boundaries = 0 <= neighbour_x < len(map) and 0 <= neighbour_y < len(map[0])

            if inside_map_boundaries and (neighbour_x, neighbour_y) != (prev_x, prev_y):
                neighbour_tile = map[neighbour_x][neighbour_y]

                possible_outs = [(neighbour_x+shifting[0], neighbour_y+shifting[1]) for shifting in tiles_mapping[neighbour_tile]]
                connected_neighbour = (current_x, current_y) in possible_outs

                if connected_neighbour:
                   
                    if created_nodes[neighbour_x][neighbour_y] is None:
                        created_nodes[neighbour_x][neighbour_y] = Node(neighbour_tile, prev=current_node)
                    else:
                        created_nodes[neighbour_x][neighbour_y].prev = current_node

                    if current_node.next is None:
                        current_node.next = created_nodes[neighbour_x][neighbour_y]
                    
                    prev_x, prev_y = current_x, current_y
                    current_x, current_y = neighbour_x, neighbour_y
                    break

    return starting_node, created_nodes


def print_loop(created_nodes: list[list]) -> None:
    belong_loop: str = "X"
    useless: str = "."

    for i in range(len(created_nodes[0])):
        line = ""
        for j in range(len(created_nodes)):
            if created_nodes[j][i] is None:
                line += useless
            else:
                line += belong_loop
        print(line)


def nest_detector(created_nodes: list[list]) -> list[list[bool]]:
    nests_map = [[(False, False) for _ in range(len(map[0]))] for _ in range(len(map))]

    for idx_col, col in enumerate(nests_map):
        for idx_row, el in enumerate(col):
            pass

    return None


def problem_1():

    lines = open_input()

    map = map_parsing(lines)
    
    starting_point = locate_starting_point(map)

    starting_node, _ = loop_finder(starting_point, map)

    max_distance = 0
    prev_cursor = starting_node.prev
    next_cursor = starting_node.next
    while prev_cursor != next_cursor:
        # NOTE: horrible possible infinite loop if even number of nodes, but isn't the case here, so it's fine
        prev_cursor = prev_cursor.prev
        next_cursor = next_cursor.next
        max_distance += 1

    return max_distance+1


def problem_2():

    lines = open_input()

    map = map_parsing(lines)

    starting_point = locate_starting_point(map)

    _, created_nodes = loop_finder(starting_point, map)

    print_loop(created_nodes)

    return nest_detector(created_nodes)


if __name__ == "__main__":
    print(problem_2())

    # choice = input("Choose which problem to print (1 or 2): ")
    
    # if choice == "1":
    #     print(problem_1())
    # elif choice == "2":
    #     print(problem_2())
    # else:
    #     print("Invalid choice. Please enter 1 or 2.")
