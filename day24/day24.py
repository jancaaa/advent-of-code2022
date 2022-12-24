from typing import List, Tuple


class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, o: object) -> bool:
        return self.x == o.x and self.y == o.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))


def read_file() -> List[List[str]]:
    with open("input.txt") as fp:
        line = fp.readline()
        valley = []
        while line:
            line = line.rstrip()
            valley.append(list(line))
            line = fp.readline()
        return valley


def move_blizzards(valley: List[List[str]]) -> List[List[str]]:
    size_x = len(valley[0])
    size_y = len(valley)
    new_valley = [["" for _ in range(size_x)] for _ in range(size_y)]
    for y in range(len(valley)):
        for x in range(len(valley[y])):
            for i in valley[y][x]:
                if i == "#":
                    new_valley[y][x] = "#"
                elif i == ">":
                    new_x = x + 1 if valley[y][x + 1] != "#" else 1
                    new_valley[y][new_x] += ">"
                elif i == "<":
                    new_x = x - 1 if valley[y][x - 1] != "#" else size_x - 2
                    new_valley[y][new_x] += "<"
                elif i == "^":
                    new_y = y - 1 if valley[y - 1][x] != "#" else size_y - 2
                    new_valley[new_y][x] += "^"
                elif i == "v":
                    new_y = y + 1 if valley[y + 1][x] != "#" else 1
                    new_valley[new_y][x] += "v"
    return new_valley


def get_path_length(valley: List[List[str]], start: Position, end: Position) -> Tuple[int, List[List[str]]]:
    time = 0
    is_end_reached = False
    positions = set()
    positions.add(start)
    while is_end_reached is False:
        time += 1
        valley = move_blizzards(valley)
        new_positions = set()
        for pos in positions:
            # stay
            if valley[pos.y][pos.x] == "":
                new_positions.add(pos)

            # left
            if valley[pos.y][pos.x - 1] == "":
                new_positions.add(Position(pos.x - 1, pos.y))

            # right
            if valley[pos.y][pos.x + 1] == "":
                new_positions.add(Position(pos.x + 1, pos.y))

            # up
            if pos.y != 0 and valley[pos.y - 1][pos.x] == "":
                new_positions.add(Position(pos.x, pos.y - 1))

            # down
            if pos.y != len(valley) - 1 and valley[pos.y + 1][pos.x] == "":
                new_positions.add(Position(pos.x, pos.y + 1))

        if end in new_positions:
            is_end_reached = True
        else:
            positions = new_positions
    return time, valley


def part1(valley: List[List[str]]) -> int:
    start = Position(1, 0)
    end = Position(len(valley[0]) - 2, len(valley) - 1)
    time, _ = get_path_length(valley, start, end)
    return time


def part2(valley: List[List[str]]) -> int:
    start = Position(1, 0)
    end = Position(len(valley[0]) - 2, len(valley) - 1)
    time1, valley = get_path_length(valley, start, end)
    time2, valley = get_path_length(valley, end, start)
    time3, valley = get_path_length(valley, start, end)

    return time1 + time2 + time3


if __name__ == "__main__":
    valley = read_file()
    print(f"Part 1: {part1(valley)}")
    print(f"Part 2: {part2(valley)}")
