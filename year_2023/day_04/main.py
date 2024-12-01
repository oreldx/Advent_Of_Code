DEBUG = False


def open_input():

    if DEBUG:
        print("DEBUG MODE ON")
        lines = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ]
    else:
        with open("input.txt", 'r') as file:
            lines = file.readlines()

        if not lines:
            return []

    return lines


def card_parser(card_string: str) -> dict:

    card_id: int = int(card_string.split(":")[0].split(" ")[-1])
    card_content: str = card_string.split(":")[-1]

    winning_numbers: list = [int(num.strip()) for num in card_content.split("|")[0].split(" ") if num != ""]
    numbers: list = [int(num.strip()) for num in card_content.split("|")[-1].split(" ") if num != ""]

    return card_id, {"winning": winning_numbers, "numbers": numbers}


def problem_1():
    points = 0

    cards_raw = open_input()
    for card_str in cards_raw:
        _, card_content = card_parser(card_str)

        card_value = 0
        for winning_number in card_content["winning"]:
            if winning_number in card_content["numbers"]:
                if card_value == 0:
                    card_value = 1
                else:
                    card_value *=2
        points += card_value

    return points


def problem_2():
    total_scratchcards: int = 0

    cards_raw = open_input()
    instances: dict = {card_id: card_content for card_id, card_content in (card_parser(card_str) for card_str in cards_raw)}

    for card_id in instances.keys():
        instances[card_id]["occ"]: int = 1

    cursor = 1
    while instances:
        for _ in range(instances[cursor]["occ"]):

            new_instances: int = 0
            for winning_number in instances[cursor]["winning"]:
                if winning_number in instances[cursor]["numbers"]:
                    new_instances += 1

            for j in range(1, new_instances+1):
                instances[cursor+j]["occ"] += 1

            total_scratchcards += 1 

        del instances[cursor]
        cursor += 1

    return total_scratchcards


if __name__ == "__main__":
    choice = input("Choose which problem to print (1 or 2): ")
    
    if choice == "1":
        print(problem_1())
    elif choice == "2":
        print(problem_2())
    else:
        print("Invalid choice. Please enter 1 or 2.")
