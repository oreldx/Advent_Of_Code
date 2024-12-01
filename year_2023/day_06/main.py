DEBUG = False


def open_input():

    if DEBUG:
        print("DEBUG MODE ON")
        lines = [
            "Time:      7  15   30",
            "Distance:  9  40  200",
        ]
    else:
        with open("input.txt", 'r') as file:
            lines = file.readlines()

        if not lines:
            return []

    return lines


def races_parser_kerned(races_list: list) -> list:

    if len(races_list) != 2:    
        raise Exception('Incorrect races input, length != 2')

    races_matrice = [[int(value) for value in race_string.split(":")[-1].strip().split(" ") if value != ''] for race_string in races_list]

    races_matrice_reversed = []
    for i in range(min([len(type)for type in races_matrice])):
            races_matrice_reversed.append([races_matrice[j][i] for j in range(len(races_matrice))])

    return races_matrice_reversed


def races_parser_unkerned(races_list: list) -> list:

    if len(races_list) != 2:    
        raise Exception('Incorrect races input, length != 2')

    races_matrice = [int(('').join(race_string.split(":")[-1].strip().split(" "))) for race_string in races_list]

    return races_matrice


def get_race_winning_range(race: list) -> tuple:
    available_duration: int = race[0]
    record: int = race[1]

    start_range = 0

    # speed == time_button_pressed (+1ms == +1mm/s)
    for speed in range(available_duration):
        distance = (available_duration - speed) * speed
        if distance > record:
            start_range = speed
            break

    end_range = start_range

    for speed in range(available_duration, -1, -1):
        distance = (available_duration - speed) * speed
        end_range = speed
        if distance > record:
            break

    return (start_range, end_range)


def problem_1():
    raw_races: list = open_input()
    
    races: list = races_parser_kerned(raw_races)

    strategies_count = 1
    for race in races:
        range_start, range_end = get_race_winning_range(race)

        if range_start != range_end:
            strategies_count *= range_end - range_start + 1

    return strategies_count


def problem_2():
    raw_races: list = open_input()
    
    single_race: list = races_parser_unkerned(raw_races)

    range_start, range_end = get_race_winning_range(single_race)

    return range_end - range_start + 1


if __name__ == "__main__":
    choice = input("Choose which problem to print (1 or 2): ")
    
    if choice == "1":
        print(problem_1())
    elif choice == "2":
        print(problem_2())
    else:
        print("Invalid choice. Please enter 1 or 2.")
