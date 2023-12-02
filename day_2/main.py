def puzzle_1():
    """Solves puzzle 1"""
    #read input text file
    input = open("day_2/input_2.txt", "rt").read()

    #split by lines
    games = input.splitlines()

    #filter the games by if they are possible
    possible_games = [game for game in games if game_is_possible(game)]

    #get the game id for the games that were possible
    possible_game_ids = [get_game_id(game) for game in possible_games]

    #add up the sums of the ids of those games
    return sum(possible_game_ids)

def puzzle_2():
    """Solves puzzle 2 and returns the answer"""

    #read input text file
    input = open("day_2/input_2.txt", "rt").read()

    #split by lines
    games = input.splitlines()

    #for each game, get the power
    game_powers = [get_game_power(game) for game in games]

    #return the sum
    return sum(game_powers)


def game_is_possible(game : str) -> bool:
    """Returns true if the game is possible"""

    #ignore the characters before the colon
    game = game[game.index(":")+1:]

    #split games into trials, at the semicolon
    trials = game.split(";")

    #see if each trial is possible
    trials_are_possible = [trial_is_possible(trial) for trial in trials]

    #return if all the trials are possible
    return all(trials_are_possible)

def get_game_id(game : str) -> int:
    """Returns the game id of the game"""

    #its always the 5th character, zero-indexed, until the colon
    return int(game[5: game.index(":")])

def trial_is_possible(trial : str) -> bool:
    """Return true if the trial is possible, false if not"""

    #split each trial by commma
    count_and_color = trial.split(",")
    count_and_color = [cnc.strip().split(" ") for cnc in count_and_color]

    #return true if all cube counts are valid in the trial
    count_and_color_valid = [is_valid_cube_count(cnc) for cnc in count_and_color]
    return all(count_and_color_valid)
    
def is_valid_cube_count(count_and_color : list) -> bool:
    """returns true if the number of cubes in the trial is at or below the limit"""
    RED_CUBES = 12
    GREEN_CUBES = 13
    BLUE_CUBES = 14

    if count_and_color[1] == "red":
        return int(count_and_color[0]) <= RED_CUBES
    elif count_and_color[1] == "green":
        return int(count_and_color[0]) <= GREEN_CUBES
    elif count_and_color[1] == "blue":
        return int(count_and_color[0]) <= BLUE_CUBES
    
def get_game_power(game : str) -> int:
    """
    Gets the power of the game
    """

    #ignore everything prior to the colon
    game = game.split(":")[1]

    #split the game by commas and semicolons
    trials = game.replace(";", ",").split(",")

    #find the maximum number for each color: red: green, blue
    colors_and_counts = [cnc.strip().split(" ") for cnc in trials]

    max_red = 0
    max_blue = 0
    max_green = 0

    for cnc in colors_and_counts:
        cnc[0] = int(cnc[0])
        if cnc[1] == "red":
            if cnc[0] > max_red:
                max_red = cnc[0]
        if cnc[1] == "blue":
            if cnc[0] > max_blue:
                max_blue = cnc[0]
        if cnc[1] == "green":
            if cnc[0] > max_green:
                max_green = cnc[0]

    return max_green*max_blue*max_red

if __name__ == "__main__":
    print(puzzle_1())
    print(puzzle_2())