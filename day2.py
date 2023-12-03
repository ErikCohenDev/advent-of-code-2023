# Day 2
# Cubes -> R G B
# which games would have been possible
# if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
def main():
    with open('./day2.txt') as file:
        print(f'The answer for part 1 is: {part1(file)}')
    with open('./day2.txt') as file:
        print(f'The answer for part 2 is: {part2(file)}')

###
# Determine games that are possible and impossible
def part1(file):
    id_sum = 0

    for line in file:
        possible = True
        game = render_game(line)
        id = game["id"]
        for game_set in game["game_sets"]:
            is_possible = determine_if_possible(game_set)
            if not is_possible:
                possible = False
                break
        if possible:
            id_sum += id
    return id_sum

###
# Receives a game string which includes
# Game ID and a set of games
# Returns a normalized dictionairy with the data from the string
# {
#   "id": 1,
#   "game_sets": [
#       { "blue": 3 , "red": 4, "green": None },
#       { "red": 1, "green": 2, "blue": 6 },
#       { "red": None, "green": 2, "blue": None },
#   ]
# }
def render_game(game):
    split_on_id = game.split(':')
    split_name_and_id = split_on_id[0].split(' ')
    game_sets = split_on_id[1].split(";")
    normalized_game_sets = []
    for game_set in game_sets:
        color_split = game_set.split(',')
        blue = [color.replace("blue", '').strip() for color in color_split if "blue" in color]
        red = [color.replace("red", '').strip() for color in color_split if "red" in color]
        green = [color.replace("green", '').strip() for color in color_split if "green" in color]
        normalized_game_sets.append({
            "blue": int(blue[0]) if blue else None,
            "red": int(red[0]) if red else None,
            "green": int(green[0]) if green else None,
        })

    return {
        "id": int(split_name_and_id[1]),
        "game_sets": normalized_game_sets
    }

assert render_game(
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
) == {
  "id": 1,
  "game_sets": [
      { "blue": 3 , "red": 4, "green": None },
      { "red": 1, "green": 2, "blue": 6 },
      { "red": None, "green": 2, "blue": None },
  ]
}, render_game(
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
)

## Determines if a game is possible or impossible
# Based on a set of predetermined rules.
# @Input { "blue": 3 , "red": 4, "green": None }
# @Returns Bool
def determine_if_possible(game_set):
    rules = { "red": 12, "green": 13, "blue": 14}
    possible = True

    if game_set["red"] and game_set["red"] > rules["red"]:
        possible = False

    if game_set["green"] and game_set["green"] > rules["green"]:
        possible = False

    if game_set["blue"] and game_set["blue"] > rules["blue"]:
        possible = False

    return possible


assert determine_if_possible({ "blue": 3 , "red": 4, "green": None }) == True, determine_if_possible({ "blue": 3 , "red": 4, "green": None })
assert determine_if_possible({ "blue": 3 , "red": 15, "green": None }) == False, determine_if_possible({ "blue": 3 , "red": 15, "green": None })


def part2(file):
    sum_power_of_game_sets = 0
    for line in file:
        game = render_game(line)
        least_needed = determine_least_cubes_needed(game["game_sets"])
        power = least_needed["green"] * least_needed["red"] * least_needed["blue"]
        sum_power_of_game_sets += power

    return sum_power_of_game_sets

def determine_least_cubes_needed(game_sets):
    min_blue = 0
    min_red = 0
    min_green = 0
    for game_set in game_sets:
        if game_set["green"] and game_set["green"] > min_green:
            min_green = game_set["green"]
        if game_set["red"] and game_set["red"] > min_red:
            min_red = game_set["red"]
        if game_set["blue"] and game_set["blue"] > min_blue:
            min_blue = game_set["blue"]

    return { "blue": min_blue or None , "red": min_red, "green": min_green }

assert determine_least_cubes_needed([
    { "blue": 3 , "red": 4, "green": None },
    { "blue": 6 , "red": 1, "green": 2 },
    { "blue": None , "red": None, "green": 2 }
]) == { "blue": 6, "red": 4, "green": 2 }, ([
    { "blue": 3 , "red": 4, "green": None },
    { "blue": 6 , "red": 1, "green": 2 },
    { "blue": None , "red": None, "green": 2 }
])

if __name__ == "__main__":
    main()

