DEBUG = False 


def open_input() -> str:    
    if DEBUG:
        print("DEBUG MODE ON")

        line: str = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

    else:
        line = ""
        with open("day_15/input.txt", 'r') as file:
            line: str = file.read().split("\n")[0]

    return line


def problem_1() -> int:

    def hash_algo(string: str) -> int:
        current_value = 0
        for c in string:
            ascii_code = ord(c)
            current_value += ascii_code
            current_value *= 17
            current_value %= 256

        return current_value
    
    line = open_input()

    total = 0
    prev_curs = 0
    for curs, c in enumerate( line ):
        if c == "," or curs == len(line)-1:
            if curs == len(line)-1:
                curs += 1
            segment = line[prev_curs:curs]
            prev_curs = curs + 1 
            total += hash_algo(segment)
            print(segment)
    return total 


def problem_2() -> int:

    data = open_input()

    return 0 


if __name__ == "__main__":
    choice = input("Choose which problem to print (1 or 2): ")
    
    if choice == "1":
        print(problem_1())
    elif choice == "2":
        print(problem_2())
    else:
        print("Invalid choice. Please enter 1 or 2.")

