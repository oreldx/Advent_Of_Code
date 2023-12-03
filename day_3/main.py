DEBUG = False


def open_input():

    if DEBUG:
        print("DEBUG MODE ON")
        lines = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]
    else:
        with open("day_3/input.txt", 'r') as file:
            lines = file.readlines()

        if not lines:
            return []

    return lines


def find_numbers(raw_str: str) -> list:
    index = []

    start_num = -1
    end_num = -1
    for idx, char in enumerate(raw_str):

        if char.isdigit():
            if start_num == -1:
                start_num = idx
        else:
            if start_num != -1:
                end_num = idx-1
        
        if start_num != -1 and end_num != -1:
            index.append((start_num, end_num))

            start_num = -1
            end_num = -1

    if start_num != -1:
        end_num = len(raw_str)-1
        index.append((start_num, end_num))

    return index


def problem_1():

    lines = open_input()

    machine_operators = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

    sum = 0
    for idx, line in enumerate(lines):
        numbers_index = find_numbers(line)

        for start, end in numbers_index:
            prev_adjacents = ""
            next_adjacents = ""

            if idx != 0:
                prev_line = lines[idx-1]
                prev_adjacents = prev_line[max(0, start-1):min(len(prev_line)-1, end+2)]
            if idx != len(lines)-1:
                next_line = lines[idx+1]
                next_adjacents = next_line[max(0, start-1):min(len(next_line)-1, end+2)]
                
            # print(f"{prev_adjacents}\n{line[start-1]}{line[start:end+1]}{line[end+1]}\n{next_adjacents}")
            all_adjacents = prev_adjacents + next_adjacents + line[start-1] + line[end+1]

            for operator in machine_operators:
                if operator in all_adjacents:
                    sum += int(line[start:end+1])
                    break
    return sum


def find_all(string: str, sub_string: str) -> list:
    occ = []
    start_idx = 0
    while True:
        pos = string.find(sub_string, start_idx)
        if pos == -1:
            break
        occ.append(pos)
        start_idx = pos + 1

    return occ


def problem_2():

    lines = open_input()

    gears = {}

    for line_idx, line in enumerate(lines):
        numbers_index = find_numbers(line)

        for start, end in numbers_index:
            prev_adjacents = ""
            next_adjacents = ""

            if line_idx != 0:
                prev_line = lines[line_idx-1]
                prev_adjacents = prev_line[max(0, start-1):min(len(prev_line)-1, end+2)]
            if line_idx != len(lines)-1:
                next_line = lines[line_idx+1]
                next_adjacents = next_line[max(0, start-1):min(len(next_line)-1, end+2)]
                
            current_adjacents = line[start-1] + line[end+1]

            found_gears = {}

            start_shift = max(0, start-1) * " "
            if "*" in prev_adjacents:
                found_gears[line_idx-1] = find_all(start_shift + prev_adjacents, "*")
            if "*" in current_adjacents:
                found_gears[line_idx] = find_all(start_shift + line[max(0, start-1):min(len(line)-1, end+2)], "*")
            if "*" in next_adjacents:
                found_gears[line_idx+1] = find_all(start_shift + next_adjacents, "*")

            for parent_idx, sub_gears in found_gears.items():
                for gear_idx in sub_gears:

                    gear_id = int(f"{parent_idx}{gear_idx}")
                    
                    if gear_id in gears:
                        gears[gear_id]["neighbours"] += 1
                        gears[gear_id]["value"] *= int(line[start:end+1])
                    else:
                        gears[gear_id] = {
                            "neighbours": 1,
                            "value": int(line[start:end+1]),
                        }
    
    return sum([gear["value"] for gear in gears.values() if gear["neighbours"] > 1])
        

if __name__ == "__main__":
    choice = input("Choose which problem to print (1 or 2): ")
    
    if choice == "1":
        print(problem_1())
    elif choice == "2":
        print(problem_2())
    else:
        print("Invalid choice. Please enter 1 or 2.")
