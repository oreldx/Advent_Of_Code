DEBUG = True
MAPS = [    
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]


from pprint import pprint

def open_input():

    file_path = "input.txt"
    if DEBUG:
        print("DEBUG MODE ON")
        file_path = "debug.txt"

    with open(file_path, 'r') as file:
        text = file.read()

    if text is None:
        return ""

    return text


def almanac_parser_v1(almanac_string: str) -> dict:

    almanac = {}

    seeds_string = almanac_string[:almanac_string.find("\n")]
    almanac["seed"] = [int(value) for value in seeds_string.split(" ")[1:]]

    maps = MAPS

    for map_idx, map in enumerate(maps):
        map_reference = map + " map:\n"

        start_content = almanac_string.find(map_reference)+len(map_reference)
        end_content = len(almanac_string) - 1
        if map_idx != len(maps)-1:
            next_map_reference = maps[map_idx+1] + " map:\n"
            end_content = almanac_string.find(next_map_reference)-2

        map_ranges =  [tuple([int(value) for value in range.split(" ")]) for range in almanac_string[start_content:end_content].split('\n')]

        almanac[map] = map_ranges
        
    return almanac


def problem_1():
    maps = MAPS
    almanac_raw: str = open_input()

    almanac: dict = almanac_parser_v1(almanac_raw)

    locations = []    
    for seed in almanac["seed"]:
        tmp_seed = seed

        for map in maps:
            for dest, start, length in almanac[map]:
                if start <= tmp_seed <= start+length:
                    tmp_seed = abs(start - tmp_seed) + dest
                    break
        locations.append(tmp_seed)

    return min(locations)

def almanac_parser_v2(almanac_string: str) -> dict:

    almanac = {}

    seeds_string = almanac_string[:almanac_string.find("\n")]
    
    raw_seeds = seeds_string.split(" ")[1:]
    seed_ranges = [raw_seeds[i:i + 2] for i in range(0, len(raw_seeds), 2)]

    maps = MAPS
    for map_idx, map in enumerate(maps):
        map_reference = map + " map:\n"

        start_content = almanac_string.find(map_reference)+len(map_reference)
        end_content = len(almanac_string) - 1
        if map_idx != len(maps)-1:
            next_map_reference = maps[map_idx+1] + " map:\n"
            end_content = almanac_string.find(next_map_reference)-2

        map_ranges =  [tuple([int(value) for value in range.split(" ")]) for range in almanac_string[start_content:end_content].split('\n')]

        almanac[map] = map_ranges
        
    return almanac

def problem_2():
    maps = MAPS
    almanac_raw: str = open_input()

    almanac_parser_v2(almanac_raw)
    
    return None


if __name__ == "__main__":
    choice = input("Choose which problem to print (1 or 2): ")
    
    if choice == "1":
        print(problem_1())
    elif choice == "2":
        print(problem_2())
    else:
        print("Invalid choice. Please enter 1 or 2.")
