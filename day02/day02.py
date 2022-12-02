def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            line = line.rstrip()
            a, b = line.split(" ")
            entries.append((a, b))
            line = fp.readline()
        return entries


class Shape:
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class Result:
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"


def translate_my_shape(my_shape: str) -> str:
    if my_shape == "X":
        my_shape = Shape.ROCK
    elif my_shape == "Y":
        my_shape = Shape.PAPER
    elif my_shape == "Z":
        my_shape = Shape.SCISSORS
    return my_shape


def score_shape(shape) -> int:
    if shape == Shape.ROCK:
        score = 1
    elif shape == Shape.PAPER:
        score = 2
    elif shape == Shape.SCISSORS:
        score = 3
    return score


def score_outcome_part1(opponents_shape: str, my_shape: str) -> int:
    if opponents_shape == my_shape:
        score = 3
    elif ((my_shape == Shape.ROCK and opponents_shape == Shape.SCISSORS)
          or (my_shape == Shape.SCISSORS and opponents_shape == Shape.PAPER)
          or (my_shape == Shape.PAPER and opponents_shape == Shape.ROCK)):
        # I win
        score = 6
    else:
        # I lose
        score = 0
    return score


def score_outcome_part2(outcome: str) -> int:
    if outcome == Result.LOSE:
        score = 0
    elif outcome == Result.DRAW:
        score = 3
    elif outcome == Result.WIN:
        score = 6
    return score


def get_winning_shape(opponents_shape: str) -> str:
    if opponents_shape == Shape.ROCK:
        my_shape = Shape.PAPER
    elif opponents_shape == Shape.PAPER:
        my_shape = Shape.SCISSORS
    elif opponents_shape == Shape.SCISSORS:
        my_shape = Shape.ROCK
    return my_shape


def get_loosing_shape(opponents_shape: str) -> str:
    if opponents_shape == Shape.ROCK:
        my_shape = Shape.SCISSORS
    elif opponents_shape == Shape.PAPER:
        my_shape = Shape.ROCK
    elif opponents_shape == Shape.SCISSORS:
        my_shape = Shape.PAPER
    return my_shape


def find_shape(opponents_shape: str, expected_result: str) -> str:
    if expected_result == Result.DRAW:
        my_shape = opponents_shape
    elif expected_result == Result.WIN:
        my_shape = get_winning_shape(opponents_shape)
    elif expected_result == Result.LOSE:
        my_shape = get_loosing_shape(opponents_shape)
    return my_shape


def part1(entries: list) -> int:
    score = 0
    for e in entries:
        opponents_shape, my_shape = e
        my_shape = translate_my_shape(my_shape)
        score += score_shape(my_shape) + score_outcome_part1(opponents_shape, my_shape)
    return score


def part2(entries: list) -> int:
    score = 0
    for e in entries:
        opponents_shape, expected_result = e
        my_shape = find_shape(opponents_shape, expected_result)
        score += score_shape(my_shape) + score_outcome_part2(expected_result)
    return score


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
