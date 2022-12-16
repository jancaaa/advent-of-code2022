def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        grid = []
        while line:
            line = line.rstrip()
            line = list(line)
            grid.append([int(e) for e in line])
            line = fp.readline()
        return grid


def is_visible(grid, x: int, y: int) -> bool:
    return (_is_visible_x_left(grid, x, y)
            or _is_visible_x_right(grid, x, y)
            or _is_visible_y_top(grid, x, y)
            or _is_visible_y_bottom(grid, x, y))


def _get_highest_tree_in_view(view: list) -> int:
    if len(view) == 0:
        return -1
    else:
        return max(view)


def _is_visible_x_left(grid, x: int, y: int) -> bool:
    current_height = grid[x][y]
    view = grid[x][0:y]
    highest = _get_highest_tree_in_view(view)
    return current_height > highest


def _is_visible_x_right(grid, x: int, y: int) -> bool:
    current_height = grid[x][y]
    view = grid[x][y + 1:]
    highest = _get_highest_tree_in_view(view)
    return current_height > highest


def _is_visible_y_top(grid, x, y) -> bool:
    current_height = grid[x][y]
    view = [grid[x][y] for x in range(0, x)]
    highest = _get_highest_tree_in_view(view)
    return current_height > highest


def _is_visible_y_bottom(grid, x, y) -> bool:
    current_height = grid[x][y]
    view = [grid[x][y] for x in range(x + 1, len(grid[x]))]
    highest = _get_highest_tree_in_view(view)
    return current_height > highest


def score_tree(grid, x: int, y: int) -> int:
    scored_tree = grid[x][y]
    view_x = grid[x]
    view_y = [grid[x][y] for x in range(len(grid))]
    left = view_x[0:y:]
    left.reverse()
    right = view_x[y + 1:]
    top = view_y[0:x]
    bottom = view_y[x + 1:]
    top.reverse()

    return (_score_direction(right, scored_tree)
            * _score_direction(left, scored_tree)
            * _score_direction(top, scored_tree)
            * _score_direction(bottom, scored_tree))


def _score_direction(trees_in_direction: list, scored_tree: int) -> int:
    score = 0
    for tree in trees_in_direction:
        score += 1
        if tree >= scored_tree:
            return score
    return score


def part1(grid) -> int:
    count = 0
    grid_size = len(grid)
    for x in range(grid_size):
        for y in range(grid_size):
            if is_visible(grid, x, y):
                count += 1
    return count


def part2(grid) -> int:
    max_score = 0
    grid_size = len(grid)
    for x in range(grid_size):
        for y in range(grid_size):
            score = score_tree(grid, x, y)
            if score > max_score:
                max_score = score
    return max_score


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
