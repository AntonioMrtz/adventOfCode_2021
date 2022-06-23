
import logging

logging.basicConfig(level=logging.WARNING)


points_per_error = {

    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137

}

points_per_missing = {

    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4

}

closing_to_opening_characters = {

    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"

}

opening_to_closing_characters = {

    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}


MULTIPLY_FACTOR = 5  # multiply factor for part 2 result

incompleted_lines = []  # stores incompleted lines in part 1 to be used in part 2


def openFile():

    archivo = open("input10.txt")
    #archivo=open("prueba.txt")

    return archivo


def get_error_score(line):

    # last open character has to be the same as first close character
    # when a chunk closes correctly we pop both out of the structures and continue

    error_score = 0

    open_characters = []
    last_close_character = ""

    for character in line:

        if character in closing_to_opening_characters:

            last_close_character = character

            if closing_to_opening_characters[character] == open_characters[-1]:

                open_characters.pop()

            else:

                logging.debug(f'part 1: bad closing character = {character}')
                error_score = points_per_error[last_close_character]
                break

        else:

            open_characters.append(character)

    if error_score == 0:
        # save incompleted lines for part2 , this are the ones that dont have any error with incorrect closing -> missing ending characters
        incompleted_lines.append(line)

    return error_score


def main_p1():  # get the first incorrect close character ONLY

    archivo = openFile()

    total_error_score = 0

    # sizes can be different from line to line

    while True:

        line = archivo.readline()

        if not line:
            break

        total_error_score += get_error_score(line.replace("\n", ""))

    return total_error_score


def get_imcompletion_score(line):

    incompletion_score = 0

    open_characters = []

    last_close_character = ""

    additions = ""

    for character in line:

        if character in closing_to_opening_characters:

            last_close_character = character

            if closing_to_opening_characters[character] == open_characters[-1]:

                open_characters.pop()

        else:

            open_characters.append(character)

    for i in range(0, len(open_characters)):

        open_characters[i] = opening_to_closing_characters[open_characters[i]]

    # manage string of additional endings characters
    # first opening character would be closed at last

    flag_first = 0

    for character in open_characters[::-1]:  # iterate in reverse order

        if flag_first == 0:
            flag_first = 1

            incompletion_score += points_per_missing[character]

        elif flag_first == 1:

            incompletion_score *= 5
            incompletion_score += points_per_missing[character]

    logging.debug(f"part 2 : partial result : {incompletion_score}")
    return incompletion_score


def main_p2():

    total_imcompletion_score = []

    for line in incompleted_lines:

        total_imcompletion_score.append(get_imcompletion_score(line))

    # Compute the median of the different scores for lines

    n = len(total_imcompletion_score)
    total_imcompletion_score.sort()

    if n % 2 == 0:
        median1 = total_imcompletion_score[n//2]
        median2 = total_imcompletion_score[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = total_imcompletion_score[n//2]

    return median


if __name__ == "__main__":
    print(f"part 1 : {main_p1()}\n")
    print(f"part 2 : {main_p2()}\n")
