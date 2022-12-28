def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            line = line.rstrip()
            entries.append(line)
            line = fp.readline()
        return entries


def convert_to_decimal(snafu: str) -> int:
    n = 0
    for i, c in enumerate(snafu[::-1]):
        if c == "-":
            c = -1
        elif c == "=":
            c = -2

        n += int(c) * pow(5, i)
    return n


def convert_to_snafu(decimal: int) -> str:
    n = ""
    f = 0
    while decimal > 0:
        r = decimal % 5 + f
        decimal = decimal // 5

        if r == 3:
            n = "=" + n
            f = 1
        elif r == 4:
            n = "-" + n
            f = 1
        elif r == 5:
            n = "0" + n
            f = 1
        else:
            n = str(r) + n
            f = 0

    n = str(f) + n

    return n.lstrip("0")


def part1(entries: list) -> str:
    sum = 0
    for e in entries:
        sum += convert_to_decimal(e)
    return convert_to_snafu(sum)


def part2(entries: list) -> int:
    return


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
