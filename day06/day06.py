def read_file() -> str:
    with open("input.txt") as fp:
        line = fp.readline()
        return line


def get_marker_index(signal: str, marker_length: int) -> int:
    marker = list(signal[:marker_length])
    for index, c in enumerate(signal[marker_length:]):
        if contains_duplicities(marker):
            marker.pop(0)  # remove first
            marker.append(c)  # add next
        else:
            return index + marker_length


def contains_duplicities(marker: list) -> bool:
    return len(set(marker)) != len(marker)


def part1(signal: str) -> int:
    return get_marker_index(signal, 4)


def part2(signal: str) -> int:
    return get_marker_index(signal, 14)


def tests_part1():
    assert part1("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert part1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert part1("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert part1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert part1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def tests_part2():
    assert part2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert part2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert part2("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert part2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert part2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26


if __name__ == "__main__":
    tests_part1()
    tests_part2()
    signal = read_file()
    print(f"Part 1: {part1(signal)}")
    print(f"Part 2: {part2(signal)}")
