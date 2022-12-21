import copy
from typing import List, Tuple


class Number:
    def __init__(self, value: int, index: int) -> None:
        self.value = value
        self.original_index = index

    def __eq__(self, o: object) -> bool:
        return self.value == o.value and self.original_index == o.original_index

    def __hash__(self) -> int:
        return hash((self.value, self.original_index))


def read_file() -> Tuple[List[Number], Number]:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        index = 0
        while line:
            line = line.rstrip()
            number = Number(int(line), index)
            entries.append(number)
            if number.value == 0:
                zero = number
            line = fp.readline()
            index += 1
        return entries, zero


def mix(list: List[Number], number: Number) -> List[Number]:
    current_index = list.index(number)
    new_index = current_index + number.value
    if current_index != new_index:
        list.pop(current_index)
        new_index = new_index % len(list)
        list.insert(new_index, number)
    return list


def get_groove_coordinates(mixed: List[Number], zero: Number):
    zero_index = mixed.index(zero)
    i1000 = (zero_index + 1000) % len(mixed)
    i2000 = (zero_index + 2000) % len(mixed)
    i3000 = (zero_index + 3000) % len(mixed)
    return mixed[i1000].value + mixed[i2000].value + mixed[i3000].value


def part1(entries: List[Number], zero: Number) -> int:
    mixed_list = copy.deepcopy(entries)
    for number in entries:
        mixed_list = mix(mixed_list, number)
    return get_groove_coordinates(mixed_list, zero)


def part2(entries: List[Number]) -> int:
    description_key = 811589153
    for e in entries:
        e.value = e.value * description_key
    mixed_list = copy.deepcopy(entries)
    for _ in range(10):
        for number in entries:
            mixed_list = mix(mixed_list, number)
    return get_groove_coordinates(mixed_list, zero)


if __name__ == "__main__":
    entries, zero = read_file()
    print(f"Part 1: {part1(entries, zero)}")
    print(f"Part 2: {part2(entries)}")
