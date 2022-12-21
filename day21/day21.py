def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        monkeys = dict()
        while line:
            line = line.rstrip()
            name, job = line.split(": ")
            monkeys[name] = job
            line = fp.readline()
        return monkeys


def get_value(name: str, monkeys: dict) -> int:
    if monkeys[name].isnumeric():
        value = monkeys[name]
        return int(value)
    else:
        v1, operation, v2 = monkeys[name].split(" ")
        if operation == "+":
            return get_value(v1, monkeys) + get_value(v2, monkeys)
        elif operation == "-":
            return get_value(v1, monkeys) - get_value(v2, monkeys)
        elif operation == "*":
            return get_value(v1, monkeys) * get_value(v2, monkeys)
        elif operation == "/":
            return get_value(v1, monkeys) // get_value(v2, monkeys)
        else:
            raise ValueError("Unknown operation", operation)


def part1(monkeys: dict) -> int:
    return get_value("root", monkeys)


def part2(monkeys: dict) -> int:
    return


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
