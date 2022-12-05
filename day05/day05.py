from typing import Tuple, List
import copy


class Instruction:
    def __init__(self, instruction: str):
        _, crate_count, _, start, _, destination = instruction.split(" ")
        self.crate_count = int(crate_count)
        self.start = int(start)
        self.destination = int(destination)


def read_file() -> Tuple[List[List[str]], List[Instruction]]:
    with open("input.txt") as fp:
        line = fp.readline()
        stacks = []

        while line != "\n":
            # stacks
            line = line.rstrip()
            stacks.insert(0, line)
            line = fp.readline()

        stacks.pop(0)  # remove stack order numbers
        stacks = _parse_stacks(stacks)

        # instructions
        line = fp.readline()
        instructions = []
        while line:
            line = line.rstrip()
            instruction = Instruction(line)
            instructions.append(instruction)
            line = fp.readline()

        return stacks, instructions


def _get_stack_count(line: str) -> int:
    line = line.rstrip().lstrip()
    return len(line) // 3


def _get_letters(line: str) -> List[str]:
    letters = []
    index = 1
    while index < len(line):
        letters.append(line[index])
        index += 4
    return letters


def _parse_stacks(stacks: List[str]) -> List[List[str]]:
    parsed_stacks = []
    count = _get_stack_count(stacks[0])
    for i in range(count):
        parsed_stacks.append([])

    for line in stacks:
        letters = _get_letters(line)
        for index, letter in enumerate(letters):
            if letter != " ":
                parsed_stacks[index].append(letter)
    return parsed_stacks


def move_part1(stacks: List[List[str]], instructions: List[Instruction]) -> list:
    moved_stacks = copy.deepcopy(stacks)
    for instruction in instructions:
        for _ in range(instruction.crate_count):
            crate = moved_stacks[instruction.start - 1].pop(-1)
            moved_stacks[instruction.destination - 1].append(crate)
    return moved_stacks


def move_part2(stacks: List[List[str]], instructions: List[Instruction]) -> list:
    moved_stacks = copy.deepcopy(stacks)
    for instruction in instructions:
        s = []
        for _ in range(instruction.crate_count):
            crate = moved_stacks[instruction.start - 1].pop(-1)
            s.insert(0, crate)
        moved_stacks[instruction.destination - 1].extend(s)
    return moved_stacks


def get_top(stacks: List[List[str]]) -> str:
    top = []
    for s in stacks:
        if len(s) == 0:
            top.append(" ")
        else:
            top.append(s[-1])
    return "".join(top)


def part1(stacks: List[List[str]], instructions: List[Instruction]) -> str:
    moved_stacks = move_part1(stacks, instructions)
    return get_top(moved_stacks)


def part2(stacks: List[List[str]], instructions: List[Instruction]) -> str:
    moved_stacks = move_part2(stacks, instructions)
    return get_top(moved_stacks)


if __name__ == "__main__":
    stacks, instructions = read_file()
    print(f"Part 1: {part1(stacks, instructions)}")
    print(f"Part 2: {part2(stacks, instructions)}")
