DEBUG = False

HANDS_STRENGTHS: list[float]  = ["five_of_kind", "four_of_kind", "full_house", "three_of_kind", "two_pair", "one_pair", "high_card"]
LABELS_STRENGTH_JOKER_FALSE: list[str]  = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
LABELS_STRENGTH_JOKER_TRUE: list[str]  = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


def open_input():    
    if DEBUG:
        print("DEBUG MODE ON")
        lines: list = [
            "32T3K 765",
            "T55J5 684",
            "KK677 28",
            "KTJJT 220",
            "QQQJA 483",
        ]
    else:
        with open("day_7/input.txt", 'r') as file:
            lines: list = file.read().split("\n")
            if lines[-1] == "":
                lines.pop(-1)

        if not lines:
            return []

    return lines


def hand_parser(hand_string: str) -> tuple:
    
    hand_string: str = hand_string.split(" ")
    cards: str = hand_string[0]
    bid: int = int(hand_string[-1])
    
    return cards, bid


def get_hand_type(hand_string: str, joker_mode: bool = False) -> str:
    hand_config: dict[str, int] = {}

    if joker_mode:
        jokers_count = sum([1 for card in hand_string if card == "J"])

    for idx_card, card in enumerate(hand_string):
        
        if joker_mode and card == "J":
            continue

        if card not in hand_config:
            hand_config[card] = 1
            for i, c in enumerate(hand_string):
                if card == c and i != idx_card:
                    hand_config[card] += 1

    if joker_mode:
        labels_strength: list[str]  = LABELS_STRENGTH_JOKER_TRUE

        if jokers_count == 5:
            hand_config = {labels_strength[-1]: 5}
        else:
            for _ in range(jokers_count):
                cards_counts: list = hand_config.values()
                
                possible_upgrade_cards = {}
                for card in hand_config.keys():
                    if hand_config[card] == max(cards_counts):
                        possible_upgrade_cards[labels_strength.index(card)] = card

                choosen_upgrade_card = possible_upgrade_cards[max(possible_upgrade_cards.keys())]
                hand_config[choosen_upgrade_card] += 1

    cards_counts: list = hand_config.values()
    hand_type: str = ""
    if len(cards_counts) == 1:
        hand_type = "five_of_kind"
    elif 4 in cards_counts:
        hand_type = "four_of_kind"
    elif 3 in cards_counts:
        if 2 in cards_counts:
            hand_type = "full_house"
        else:
            hand_type = "three_of_kind"
    elif len(cards_counts) == 3 and 3 not in cards_counts:
        hand_type = "two_pair"
    elif len(cards_counts) == 5:
        hand_type = "high_card"
    else:
        hand_type = "one_pair"

    return hand_type

def second_ordering(hands_list: list, joker_mode: bool = False) -> list:
    
    labels_strength: list[str]  = LABELS_STRENGTH_JOKER_FALSE
    if joker_mode:
        labels_strength: list[str]  = LABELS_STRENGTH_JOKER_TRUE
    
    for i in range(len(hands_list)):
        min_index = i
        for j in range(i + 1, len(hands_list)):
            
            for k in range(5):
                if labels_strength.index(hands_list[j][0][k]) > labels_strength.index(hands_list[min_index][0][k]):
                    break
                if labels_strength.index(hands_list[j][0][k]) < labels_strength.index(hands_list[min_index][0][k]):
                    min_index = j
                    break

        hands_list[i], hands_list[min_index] = hands_list[min_index], hands_list[i]

    return hands_list


def problem_1():
    hands_list: list = open_input()

    hands: dict[str, list[tuple[str, int]]] = {}
    # First ordering, by hand type
    for hand_raw in hands_list:
        hand_string, bid = hand_parser(hand_raw)

        hand_type: str = get_hand_type(hand_string)

        if hand_type not in hands:
            hands[hand_type] = [(hand_string, bid)]
        else:
            hands[hand_type].append((hand_string, bid))

    hands_strengths: list[float]  = HANDS_STRENGTHS
    
    total_winnings: int = 0
    rank: int = 1
    for hand_strength in hands_strengths[::-1]:
        if hand_strength in hands:
            
            hands[hand_strength] = second_ordering(hands[hand_strength])

            for hand in hands[hand_strength]:
                bid = hand[1]
                total_winnings += bid * rank
                rank += 1

    return total_winnings

def problem_2():
    hands_list: list = open_input()

    hands: dict[str, list[tuple[str, int]]] = {}

    # First ordering, by hand type
    for hand_raw in hands_list:
        hand_string, bid = hand_parser(hand_raw)

        hand_type: str = get_hand_type(hand_string, joker_mode=True)

        if hand_type not in hands:
            hands[hand_type] = [(hand_string, bid)]
        else:
            hands[hand_type].append((hand_string, bid))

    hands_strengths = HANDS_STRENGTHS

    total_winnings: int = 0
    rank: int = 1
    for hand_strength in hands_strengths[::-1]:
        if hand_strength in hands:
            
            hands[hand_strength] = second_ordering(hands[hand_strength], joker_mode=True)

            for hand in hands[hand_strength]:
                bid = hand[1]
                total_winnings += bid * rank
                rank += 1

    return total_winnings

if __name__ == "__main__":
    choice = input("Choose which problem to print (1 or 2): ")
    
    if choice == "1":
        print(problem_1())
    elif choice == "2":
        print(problem_2())
    else:
        print("Invalid choice. Please enter 1 or 2.")
