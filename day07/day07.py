from typing import Tuple, Dict, List


class Directory:
    def __init__(self, dirs: List[str], files: List[int]):
        self.dirs = dirs
        self.files = files
        self.size = None


def read_file() -> List[Tuple[str, List[str]]]:
    # returned format: (instruction, output)
    with open("input.txt") as fp:
        line = fp.readline()
        instructions = []
        cmd_result = []
        while line:
            line = line.rstrip()
            if line.startswith("$"):
                if len(cmd_result) != 0:
                    # save ls output
                    instructions.append(("$ ls", cmd_result))
                    cmd_result = []
                if line.startswith("$ cd"):
                    instructions.append((line, []))
            else:
                # process ls result
                cmd_result.append(line)
            line = fp.readline()
        if len(cmd_result) != 0:
            # save ls output
            instructions.append(("$ ls", cmd_result))
        return instructions


def get_dir_contents(instructions: List[Tuple[str, List[str]]]) -> Dict[str, Directory]:
    dirs = dict()
    current_path = []
    for c, output in instructions:
        if c.startswith("$ cd .."):
            current_path.pop(-1)
        elif c.startswith("$ cd "):
            _, _, dir = c.split(" ")
            current_path.append(dir)
        else:
            # ls
            path = "/".join(current_path)
            dirs[path] = parse_dir_content(output)
    return dirs


def parse_dir_content(ls_output: str) -> Directory:
    dirs = []
    files = []
    for c in ls_output:
        x, y = c.split(" ")
        if x == "dir":
            # dir with name y
            dirs.append(y)
        else:
            # file with size x
            files.append(int(x))
    return Directory(dirs, files)


def get_dir_size(path: str, dirs: Dict[str, Directory]) -> Dict[str, Directory]:
    current_dir = dirs[path]
    if current_dir.size is None:
        size = 0
        # sum of file sizes
        for file in current_dir.files:
            size += file

        # sum of dirs sizes
        for d in current_dir.dirs:
            sub_dir_path = path + "/" + d
            sub_dir = dirs[sub_dir_path]
            if sub_dir.size is None:
                # calculate if not calculated
                dirs = get_dir_size(sub_dir_path, dirs)
            size += sub_dir.size

        # set dir size
        current_dir.size = size
    return dirs


def part1(dirs: Dict[str, Directory]) -> int:
    sum = 0
    for d in dirs.keys():
        size = dirs[d].size
        if size <= 100000:
            sum += size
    return sum


def part2(dirs: Dict[str, Directory]) -> int:
    free_space = 70000000 - dirs["/"].size
    required_space = 30000000
    must_be_removed = required_space - free_space
    smallest_dir_to_remove_size = required_space
    for dir in dirs.keys():
        dir_size = dirs[dir].size
        if dir_size < smallest_dir_to_remove_size and dir_size > must_be_removed:
            smallest_dir_to_remove_size = dir_size
    return smallest_dir_to_remove_size


if __name__ == "__main__":
    instructions = read_file()
    contents = get_dir_contents(instructions)
    dirs = get_dir_size("/", contents)
    print(f"Part 1: {part1(dirs)}")
    print(f"Part 2: {part2(dirs)}")
