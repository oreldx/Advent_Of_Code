DEBUG = False


def open_input():    
    if DEBUG:
        print("DEBUG MODE ON")
        # lines: list = [
        #     "RL",
        #     "",
        #     "AAA = (BBB, CCC)",
        #     "BBB = (DDD, EEE)",
        #     "CCC = (ZZZ, GGG)",
        #     "DDD = (DDD, DDD)",
        #     "EEE = (EEE, EEE)",
        #     "GGG = (GGG, GGG)",
        #     "ZZZ = (ZZZ, ZZZ)",
        # ]

        # lines: list = [
        #     "LLR",
        #     "",
        #     "AAA = (BBB, BBB)",
        #     "BBB = (AAA, ZZZ)",
        #     "ZZZ = (ZZZ, ZZZ)",
        # ]

        lines: list = [
            "LR",
            "",
            "11A = (11B, XXX)",
            "11B = (XXX, 11Z)",
            "11Z = (11B, XXX)",
            "22A = (22B, XXX)",
            "22B = (22C, 22C)",
            "22C = (22Z, 22Z)",
            "22Z = (22B, 22B)",
            "XXX = (XXX, XXX)",
        ]
    else:
        with open("input.txt", 'r') as file:
            lines: list = file.read().split("\n")
            if lines[-1] == "":
                lines.pop(-1)

        if not lines:
            return []

    return lines


class Node:
    def __init__(self, value: str, left = None, right = None) -> None:
        self.value = value
        
        self.left = left
        self.right = right


def documents_parser_V1(documents: list) -> tuple[str, Node]:

    instructions: str = documents[0]

    network = None
    created_nodes = {}
    for line in documents[2::]:
        node_value, *_, node_dest = line.split(" = ")
        dest_left, *_, dest_right = node_dest[1:-1].split(", ")

        if dest_left not in created_nodes:
            created_nodes[dest_left] = Node(dest_left)
        node_left: Node = created_nodes[dest_left]
        
        if dest_right not in created_nodes:
            created_nodes[dest_right] = Node(dest_right)
        node_right: Node = created_nodes[dest_right]

        if node_value not in created_nodes:
            created_nodes[node_value] = Node(node_value, node_left, node_right)
        new_node = created_nodes[node_value]

        new_node.left = node_left
        new_node.right = node_right

        if network is None and node_value == "AAA":
            network: Node = new_node

    return instructions, network


def documents_parser_V2(documents: list) -> tuple[str, Node]:

    instructions: str = documents[0]

    created_nodes = {}
    starting_nodes = []
    for line in documents[2::]:
        node_value, *_, node_dest = line.split(" = ")
        dest_left, *_, dest_right = node_dest[1:-1].split(", ")

        if dest_left not in created_nodes:
            created_nodes[dest_left] = Node(dest_left)
        node_left: Node = created_nodes[dest_left]
        
        if dest_right not in created_nodes:
            created_nodes[dest_right] = Node(dest_right)
        node_right: Node = created_nodes[dest_right]

        if node_value not in created_nodes:
            created_nodes[node_value] = Node(node_value, node_left, node_right)
        new_node = created_nodes[node_value]

        new_node.left = node_left
        new_node.right = node_right

        if node_value[-1] == "A" and new_node not in starting_nodes:
            starting_nodes.append(new_node)

    return instructions, starting_nodes


def travel(node: Node, turn: str) -> Node:
    match turn:
        case "L":
            return node.left
        case "R":
            return node.right
        case _:
            raise Exception("Wrong turn value : str")


def problem_1():

    lines = open_input()

    instructions, network = documents_parser_V1(lines)

    cursor = 0
    steps = 0
    while network.value != "ZZZ":
        network = travel(network, instructions[cursor])

        steps += 1
        if cursor == len(instructions)-1:
            cursor = 0
        else: 
            cursor += 1

    return steps


def problem_2():

    def greatest_common_divisor(a, b):
        while b:
            a, b = b, a % b
        return a

    def least_common_multiple(a, b):
        return abs(a * b) // greatest_common_divisor(a, b)

    lines = open_input()

    instructions, starting_nodes = documents_parser_V2(lines)

    iterations = [0 for _ in range(len(starting_nodes))]
    for idx, starting_node in enumerate(starting_nodes):
        cursor = 0
        while not starting_node.value[-1] == "Z":

            iterations[idx] += 1

            starting_node = travel(starting_node, instructions[cursor])
            
            if cursor == len(instructions)-1:
                cursor = 0
            else: 
                cursor += 1
        
    current_lcm = iterations[0]
    for number in iterations[1:]:
        current_lcm = least_common_multiple(current_lcm, number)

    return current_lcm


if __name__ == "__main__":
    choice = input("Choose which problem to print (1 or 2): ")
    
    if choice == "1":
        print(problem_1())
    elif choice == "2":
        print(problem_2())
    else:
        print("Invalid choice. Please enter 1 or 2.")
