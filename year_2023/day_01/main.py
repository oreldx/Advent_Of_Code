import re


def open_input():
    with open("calibration_document.txt", 'r') as file:
        lines = file.readlines()

    if not lines:
        return []

    return lines
    

def problem_1():
    digits_list = [re.findall(r'\d+', line) for line in open_input()]

    sum = 0
    for digits in digits_list:
        number = ""
        digit = ("").join(digits)
        if len(digit) > 0:
            number += digit[0]

            if len(digit) == 1:
                number += digit[0]
            else:
                number += digit[-1]

            sum += int(number)

    return sum


def find_all_substrings(main_string, substring):
    start = 0
    idx = []
    while True:
        index = main_string.find(substring, start)
        if index == -1:
            break
        idx.append(index)
        start = index + 1
    return idx

def problem_2():
    conversion = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",] 

    lines = open_input()

    sum = 0
    for line in lines:
        
        found_numbers_str = {i:[] for i in range(len(conversion))}
        for number_str in conversion:
            number_int = conversion.index(number_str)

            for number_representation in [number_str, number_int]:

                occ = find_all_substrings(line, str(number_representation))

                if occ != -1:
                    found_numbers_str[number_int] += occ

        min_value = float("inf")
        min_key = None
        max_value = -1
        max_key = None
        for key, values in found_numbers_str.items():
            if values:
                tmp_min = min(values)
                tmp_max = max(values)
                if tmp_min < min_value:
                    min_value = tmp_min
                    min_key = key
                if tmp_max > max_value:
                    max_value = tmp_max
                    max_key = key

        sum += int(str(min_key)+str(max_key))

    return sum


if __name__ == "__main__":
    choice = input("Choose which problem to print (1 or 2): ")
    
    if choice == "1":
        print(problem_1())
    elif choice == "2":
        print(problem_2())
    else:
        print("Invalid choice. Please enter 1 or 2.")
