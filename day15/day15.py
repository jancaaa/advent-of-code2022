from typing import Tuple


class Coordinates:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            line = line.rstrip()
            s, b = line.split(": ")
            s = s[10:]
            b = b[21:]
            entries.append((get_coordinates(s), get_coordinates(b)))
            line = fp.readline()
        return entries


def get_coordinates(point: str) -> Coordinates:
    x, y = point.split(", ")
    return Coordinates(int(x[2:]), int(y[2:]))


def get_sensor_beacon_distance(entry: Tuple[Coordinates, Coordinates]) -> int:
    s, b = entry
    return abs(s.x - b.x) + abs(s.y - b.y)


def part1(entries: list) -> int:
    y = 2000000
    sensors = set()
    beacons = set()
    covered = set()

    for e in entries:
        s, b = e
        if s.y == y:
            sensors.add(s.x)
        if b.y == y:
            beacons.add(b.x)
        sbd = get_sensor_beacon_distance(e)
        max_x = sbd - abs(s.y - y)
        for x in range(s.x - max_x, s.x + max_x + 1):
            d = abs(s.x - x) + abs(s.y - y)
            if d <= sbd:
                covered.add(x)
        empty = covered.difference(sensors).difference(beacons)  # remove S and B
    return len(empty)


def part2(entries: list) -> int:
    return


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
