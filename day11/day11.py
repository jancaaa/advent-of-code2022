from typing import List


class Monkey:
    def __init__(self, items: str, operation: str, test: str, if_true: str, if_false: str):
        self.items = [int(item) for item in items.split(", ")]
        self.operation = operation
        self.test = int(test)
        self.if_true = int(if_true)
        self.if_false = int(if_false)
        self.items_inspected = 0


def read_file() -> List[Monkey]:
    with open("input.txt") as fp:
        line = fp.readline()
        monkeys = []
        while line:
            if line.startswith("Monkey"):
                _, items = fp.readline().rstrip().split(": ")
                _, operation = fp.readline().rstrip().split(": new = ")
                _, test = fp.readline().rstrip().split(" divisible by ")
                _, if_true = fp.readline().rstrip().split(" throw to monkey ")
                _, if_false = fp.readline().rstrip().split(" throw to monkey ")
                monkey = Monkey(items, operation, test, if_true, if_false)
                monkeys.append(monkey)
            line = fp.readline()  # /n
        return monkeys


def process(operation: str, worry_level: int) -> int:
    operation = operation.replace("old", str(worry_level))
    param1, operator, param2 = operation.split(" ")
    if operator == "*":
        worry_level = int(param1) * int(param2)
    elif operator == "+":
        worry_level = int(param1) + int(param2)
    else:
        raise ValueError("Unknown operator", operation)
    return worry_level


def play(monkeys: List[Monkey]) -> List[Monkey]:
    for monkey in monkeys:
        while monkey.items:
            item = monkey.items.pop(0)
            monkey.items_inspected += 1
            new_worry_level = process(monkey.operation, item) // 3
            index = monkey.if_true if new_worry_level % monkey.test == 0 else monkey.if_false
            monkeys[index].items.append(new_worry_level)
        monkey.items = []
    return monkeys


def part1(monkeys: List[Monkey]) -> int:
    for i in range(20):
        monkeys = play(monkeys)
    items_inspected = [e.items_inspected for e in monkeys]
    items_inspected.sort(reverse=True)
    return items_inspected[0] * items_inspected[1]


def part2(monkeys: List[Monkey]) -> int:
    return


if __name__ == "__main__":
    monkeys = read_file()
    print(f"Part 1: {part1(monkeys)}")
    print(f"Part 2: {part2(monkeys)}")
