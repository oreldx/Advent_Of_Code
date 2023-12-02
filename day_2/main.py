

def open_input():
    with open("day_2/input.txt", 'r') as file:
        lines = file.readlines()

    if not lines:
        return []

    return lines


def game_parser(game_str: str) -> dict:

    game_id = game_str.split(":")[0].split(" ")[-1]

    colors = ["red", "green", "blue"]
    sets_str = game_str.split(":")[-1].strip().split(";")

    sets = []
    for set_str in sets_str:
        set = {color: 0 for color in colors}

        for color in colors:
            idx = set_str.find(color)
            if idx != -1:
                set[color] = int(set_str[0:idx-1].split(",")[-1].strip())

        sets.append(set)

    return game_id, sets

def problem_1():

    REQUIERED_CONFIG = {"red": 12, "green": 13, "blue": 14}

    games_list = open_input()

    game_ids = []
    for game_str in games_list:
        game_id, sets = game_parser(game_str)

        max_set = set = {color: 0 for color in REQUIERED_CONFIG.keys()}
        for set in sets:
            for color in REQUIERED_CONFIG.keys():
                max_set[color] = max([max_set[color], int(set[color])])

        all_threshold = True
        for color, max_count in REQUIERED_CONFIG.items():
            if max_count < max_set[color]:
                all_threshold = False

        if all_threshold:
            game_ids.append(int(game_id))

    return sum(game_ids)


def problem_2():

    REQUIERED_CONFIG = {"red": 12, "green": 13, "blue": 14}

    games_list = open_input()

    sum = 0
    for game_str in games_list:
        _, sets = game_parser(game_str)

        max_set = set = {color: 0 for color in REQUIERED_CONFIG.keys()}
        for set in sets:
            for color in REQUIERED_CONFIG.keys():
                max_set[color] = max([max_set[color], int(set[color])])

        power = 1
        for max_color in max_set.values():
            power *= max_color
        
        sum += power

    return sum


if __name__ == "__main__":
    choice = input("Choose which problem to print (1 or 2): ")
    
    if choice == "1":
        print(problem_1())
    elif choice == "2":
        print(problem_2())
    else:
        print("Invalid choice. Please enter 1 or 2.")
