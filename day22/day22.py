from typing import Union, List, Tuple


class Position:

    def __init__(self, x, y, direction) -> None:
        self.x = x
        self.y = y
        self.direction = direction


def read_file() -> Tuple[List[List[str]], List[Union[str, int]]]:
    with open("input.txt") as fp:
        line = fp.readline()
        board = []
        while line != "\n":
            line = line.rstrip()
            board.append(list(line))
            line = fp.readline()

        # add empty tiles to the right
        max_row_len = max([len(line) for line in board])
        for line in board:
            filling = [" " for _ in range(max_row_len - len(line))]
            line.extend(filling)
        line = fp.readline()  # /n
        line = line.rstrip()
        instructions = _process_instructions(line)
        return board, instructions


def _process_instructions(instructions: str) -> List[Union[str, int]]:
    parsed_instructions = []
    instr = ""
    for i in instructions:
        if i.isdigit():
            instr += i
        else:
            parsed_instructions.append(int(instr))
            instr = ""
            parsed_instructions.append(i)
    if instr != "":
        parsed_instructions.append(int(instr))
    return parsed_instructions


def _get_direction_value(direction: str) -> int:
    if direction == "R":
        return 0
    elif direction == "D":
        return 1
    elif direction == "L":
        return 2
    elif direction == "U":
        return 3


def move(board: List[List[str]], position: Position, instruction: Union[int, str]) -> Position:
    directions = ["R", "D", "L", "U"]
    if instruction == "R":
        position.direction = directions[(directions.index(position.direction) + 1) % 4]
    elif instruction == "L":
        position.direction = directions[(directions.index(position.direction) - 1) % 4]
    else:
        if position.direction == "R" or position.direction == "L":
            step = 1 if position.direction == "R" else -1
            for i in range(instruction):
                new_x = position.x + step

                # wrap if needed
                if new_x < 0:
                    # reappear at the end line
                    new_x = len(board[position.y]) - 1
                elif new_x >= len(board[position.y]):
                    # reappear at the beginning line
                    new_x = 0

                if board[position.y][new_x] == " ":
                    if position.direction == "R":
                        new_x = 0
                    elif position.direction == "L":
                        new_x = len(board[position.y]) - 1

                    while board[position.y][new_x] == " ":
                        new_x += step

                if board[position.y][new_x] == ".":
                    # move
                    position.x = new_x
                else:
                    # wall
                    break
        elif position.direction == "U" or position.direction == "D":
            step = 1 if position.direction == "D" else -1
            for i in range(instruction):
                new_y = position.y + step

                # wrap if needed
                if new_y < 0:
                    # reappear at the bottom
                    new_y = len(board) - 1
                elif new_y >= len(board):
                    # reappear at the top
                    new_y = 0

                if board[new_y][position.x] == " ":
                    if position.direction == "U":
                        new_y = len(board) - 1
                    elif position.direction == "D":
                        new_y = 0

                    while board[new_y][position.x] == " ":
                        new_y += step

                if board[new_y][position.x] == ".":
                    # move
                    position.y = new_y
                else:
                    # wall
                    break

    return position


def part1(board: List[List[str]], instructions: List[Union[str, int]]) -> int:
    pos = Position(board[0].index("."), 0, "R")

    for i in instructions:
        pos = move(board, pos, i)

    return (pos.x + 1) * 4 + (pos.y + 1) * 1000 + _get_direction_value(pos.direction)


def part2(board: List[List[str]], instructions: List[Union[str, int]]) -> int:
    return


if __name__ == "__main__":
    board, instructions = read_file()
    # test()
    print(f"Part 1: {part1(board, instructions)}")
    print(f"Part 2: {part2(board, instructions)}")
