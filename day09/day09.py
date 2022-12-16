class Motion:
    def __init__(self, direction: str, step_count: str):
        self.direction = direction
        self.step_count = int(step_count)


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, o) -> bool:
        return self.x == o.x and self.y == o.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))


def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        motions = []
        while line:
            line = line.rstrip()
            direction, steps = line.split(" ")
            motions.append(Motion(direction, steps))
            line = fp.readline()
        return motions


def move(head_position: Position, tail_position: Position, motion: Motion):
    tail_visited = []
    for step in range(motion.step_count):
        if motion.direction == "R":
            head_position.x += 1
        elif motion.direction == "L":
            head_position.x -= 1
        elif motion.direction == "U":
            head_position.y += 1
        elif motion.direction == "D":
            head_position.y -= 1
        tail_position = move_tail(head_position, tail_position)
        tail_visited.append(tail_position)
    return head_position, tail_position, tail_visited


def move_tail(head_position: Position, tail_position: Position) -> Position:
    if abs(head_position.x - tail_position.x) <= 1 and abs(head_position.y - tail_position.y) <= 1:
        # ok -> no need to move
        return Position(tail_position.x, tail_position.y)
    elif head_position.x == tail_position.x and head_position.y > tail_position.y:
        return Position(tail_position.x, tail_position.y + 1)
    elif head_position.x == tail_position.x and head_position.y < tail_position.y:
        return Position(tail_position.x, tail_position.y - 1)
    elif head_position.x > tail_position.x and head_position.y == tail_position.y:
        return Position(tail_position.x + 1, tail_position.y)
    elif head_position.x < tail_position.x and head_position.y == tail_position.y:
        return Position(tail_position.x - 1, tail_position.y)
    else:
        # diagonal
        new_x = tail_position.x + 1 if head_position.x > tail_position.x else tail_position.x - 1
        new_y = tail_position.y + 1 if head_position.y > tail_position.y else tail_position.y - 1
        return Position(new_x, new_y)


def part1(motions: list) -> int:
    head_position = Position(0, 0)
    tail_position = Position(0, 0)
    tail_visited = set()
    tail_visited.add(tail_position)
    for motion in motions:
        head_position, tail_position, visited = move(head_position, tail_position, motion)
        tail_visited.update(visited)
    return len(tail_visited)


def part2(motions: list) -> int:
    return


if __name__ == "__main__":
    motions = read_file()
    print(f"Part 1: {part1(motions)}")
    print(f"Part 2: {part2(motions)}")
