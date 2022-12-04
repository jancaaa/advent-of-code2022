def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            line = line.rstrip()
            s1, s2 = line.split(",")
            entries.append((s1, s2))
            line = fp.readline()
        return entries


def _parse_section(section: str) -> tuple:
    s1, s2 = section.split("-")
    return int(s1), int(s2)


def is_fully_overlapping(s1: str, s2: str) -> bool:
    s1s, s1e = _parse_section(s1)
    s2s, s2e = _parse_section(s2)

    return (s1s <= s2s and s1e >= s2e) or (s2s <= s1s and s2e >= s1e)


def is_overlapping(s1: str, s2: str) -> bool:
    s1s, s1e = _parse_section(s1)
    s2s, s2e = _parse_section(s2)
    return s2s <= s1e and s1s <= s2e


def tests_part1():
    assert is_fully_overlapping("2-4", "6-8") is False
    assert is_fully_overlapping("2-3", "4-5") is False
    assert is_fully_overlapping("5-7", "7-9") is False
    assert is_fully_overlapping("2-8", "3-7") is True
    assert is_fully_overlapping("6-6", "4-6") is True
    assert is_fully_overlapping("2-6", "4-8") is False


def tests_part2():
    assert is_overlapping("2-4", "6-8") is False
    assert is_overlapping("2-3", "4-5") is False
    assert is_overlapping("5-7", "7-9") is True
    assert is_overlapping("2-8", "3-7") is True
    assert is_overlapping("6-6", "4-6") is True
    assert is_overlapping("2-6", "4-8") is True


def part1(entries: list) -> int:
    count = 0
    for s1, s2 in entries:
        if is_fully_overlapping(s1, s2):
            count += 1
    return count


def part2(entries: list) -> int:
    count = 0
    for s1, s2 in entries:
        if is_overlapping(s1, s2):
            count += 1
    return count


if __name__ == "__main__":
    tests_part1()
    tests_part2()
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
