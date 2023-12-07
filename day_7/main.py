DEBUG = False


def open_input():

    if DEBUG:
        print("DEBUG MODE ON")
        lines = [
            "32T3K 765",
            "T55J5 684",
            "KK677 28",
            "KTJJT 220",
            "QQQJA 483",
        ]
    else:
        with open("day_7/input.txt", 'r') as file:
            lines = file.read().split("\n")
            if lines[-1] == "":
                lines.pop(-1)

        if not lines:
            return []

    return lines


def hand_parser(hand_string: str) -> tuple  :
    
    hand_string = hand_string.split(" ")

    bid = 0
    cards = []

    cards = [c for c in hand_string[0]]
    bid = int(hand_string[-1])
    
    return cards, bid

def problem_1():
    hands_list: list = open_input()
    
    for hand_string in hands_list:
        print(hand_parser(hand_string))
    
    return None


def problem_2():
    pass

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
