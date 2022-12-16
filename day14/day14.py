from typing import List, Tuple


class Coordinates:
    def __init__(self, s: str) -> None:
        x, y = s.split(",")
        self.x = int(x)
        self.y = int(y)


def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        paths = []
        while line:
            line = line.rstrip()
            line = line.split(" -> ")
            line = list(map(Coordinates, line))
            paths.append(line)
            line = fp.readline()
        return paths


def generate_grid(size_x: int, size_y: int) -> List[List[str]]:
    grid = [[] for _ in range(size_y)]
    for y in range(len(grid)):
        grid[y] = [" " for _ in range(size_x)]
    return grid


def place_rocks(grid: List[List[str]], entries: list) -> List[List[str]]:
    for entry in entries:
        for i in range(len(entry) - 1):
            s = entry[i]
            e = entry[i + 1]

            if s.x == e.x:
                start, end = get_start_end(s.y, e.y)
                for y in range(start, end + 1):
                    grid[y][s.x] = "R"

            elif s.y == e.y:
                start, end = get_start_end(s.x, e.x)
                for x in range(start, end + 1):
                    grid[s.y][x] = "R"
    return grid


def get_start_end(a: int, b: int) -> Tuple[int, int]:
    start = min(a, b)
    end = max(a, b)
    return start, end


def place_sand(grid: List[List[str]]) -> Tuple[bool, List[List[str]]]:
    x = 500
    y = 0
    while True:
        if y == len(grid) - 1:
            # abyss
            return False, grid
        if grid[y + 1][x] == " ":  # down
            y += 1
        elif grid[y + 1][x - 1] == " ":  # down + left
            y += 1
            x -= 1
        elif grid[y + 1][x + 1] == " ":  # down + right
            y += 1
            x += 1
        else:
            grid[y][x] = "S"
            return True, grid


def part1(entries: list) -> int:
    size_x = 530
    size_y = 180
    grid = generate_grid(size_x, size_y)
    grid = place_rocks(grid, entries)

    count = 0
    placed = True
    while placed:
        count += 1
        placed, grid = place_sand(grid)
    return count - 1


def part2(entries: list) -> int:
    return


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
