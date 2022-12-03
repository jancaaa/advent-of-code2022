import string


def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            line = line.rstrip()
            entries.append(line)
            line = fp.readline()
        return entries


def get_item_in_both_compartments(line: str) -> str:
    l = len(line)
    c1 = line[0: l // 2]
    c2 = line[l // 2:l]
    common = set(c1).intersection(c2)
    return common.pop()


def get_priority(item: str) -> int:
    return string.ascii_letters.index(item) + 1


def get_badge(group: list) -> str:
    badge = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
    return badge.pop()


def part1(entries: list) -> int:
    sum = 0
    for e in entries:
        common_item = get_item_in_both_compartments(e)
        sum += get_priority(common_item)
    return sum


def part2(entries: list) -> int:
    sum = 0
    group = []
    for index, e in enumerate(entries):
        group.append(e)
        if index % 3 == 2:
            badge = get_badge(group)
            sum += get_priority(badge)
            group = []
    return sum


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
