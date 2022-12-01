def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        current = []
        while line:
            line = line.rstrip()
            if line == '':
                entries.append(current)
                current = []
            else:
                current.append(int(line))
            line = fp.readline()
        return entries


def sum_calories(entries: list) -> list:
    sums = []
    for e in entries:
        current = sum(e)
        sums.append(current)
    return sums


def part1(entries: list) -> int:
    sums = sum_calories(entries)
    return max(sums)


def part2(entries: list) -> int:
    sums = sum_calories(entries)
    sums.sort(reverse=True)
    return sums[0] + sums[1] + sums[2]


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
