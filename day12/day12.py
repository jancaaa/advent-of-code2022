import copy
from typing import List, Tuple


class Coordinates:
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
        entries = []
        while line:
            line = line.rstrip()
            line = list(line)
            entries.append(line)
            line = fp.readline()
        return entries


def get_start(grid: List[List[str]]) -> Coordinates:
    return _get_letter(grid, "S")


def get_starts(grid: List[List[str]]) -> List[Coordinates]:
    starts = []
    size_x = len(grid)
    size_y = len(grid[0])
    for x in range(size_x):
        for y in range(size_y):
            if grid[x][y] == "a":
                starts.append(Coordinates(x, y))
    return starts


def get_end(grid: List[List[str]]) -> Coordinates:
    return _get_letter(grid, "E")


def _get_letter(grid: List[List[str]], letter: str) -> Coordinates:
    size_x = len(grid)
    size_y = len(grid[0])
    for x in range(size_x):
        for y in range(size_y):
            if grid[x][y] == letter:
                return Coordinates(x, y)


def get_possible_next_steps(grid: List[List[str]], position: Coordinates, visited: List[Coordinates]) -> List[Coordinates]:
    up = Coordinates(position.x, position.y + 1)
    down = Coordinates(position.x, position.y - 1)
    left = Coordinates(position.x - 1, position.y)
    right = Coordinates(position.x + 1, position.y)
    possibilities = [up, down, left, right]
    next = []
    size_x = len(grid)
    size_y = len(grid[0])
    for item in possibilities:
        if 0 <= item.x < size_x and 0 <= item.y < size_y and item not in visited:
            if (ord(grid[position.x][position.y]) + 1 == ord(grid[item.x][item.y])
                    or ord(grid[position.x][position.y]) > ord(grid[item.x][item.y])
                    or ord(grid[position.x][position.y]) == ord(grid[item.x][item.y])):
                next.append(item)
    return next


def get_shortest_path(grid: List[List[str]], start: Coordinates, end: Coordinates) -> List[Coordinates]:
    visited = []
    q = []
    q.append([start])
    visited.append(start)

    while q:
        path = q.pop(0)

        if path[-1] != end:
            next = get_possible_next_steps(grid, path[-1], visited)
            for n in next:
                new_path = list(path)
                new_path.append(n)
                q.append(new_path)
            visited.extend(next)
        else:
            return path


def prepare_grid(grid: List[List[str]]) -> Tuple[List[List[str]], Coordinates, Coordinates]:
    grid = copy.deepcopy(grid)
    start = get_start(grid)
    end = get_end(grid)

    grid[start.x][start.y] = "a"
    grid[end.x][end.y] = "z"
    return grid, start, end


def part1(grid: List[List[str]]) -> int:
    grid, start, end = prepare_grid(grid)
    path = get_shortest_path(grid, start, end)
    return len(path) - 1


def part2(grid: List[List[str]]) -> int:
    grid, _, end = prepare_grid(grid)
    starts = get_starts(grid)
    shortest = len(grid) * len(grid[0])
    for s in starts:
        path = get_shortest_path(grid, s, end)
        if path and len(path) - 1 < shortest:
            shortest = len(path) - 1

    return shortest


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
