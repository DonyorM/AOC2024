import utils


def find_block(map, start_loc, dir):
    x_diff, y_diff = dir
    current_x, current_y = start_loc

    paths = set()

    while True:
        if (
            current_x < 0
            or current_x >= len(map[0])
            or current_y < 0
            or current_y >= len(map)
        ):
            return True, paths, (current_x - x_diff, current_y - y_diff)

        if map[current_y][current_x] == "#":
            return False, paths, (current_x - x_diff, current_y - y_diff)

        paths.add((current_x, current_y))
        current_x += x_diff
        current_y += y_diff


def find_start(map):
    for y in range(len(map)):
        start_x = map[y].find("^")
        if start_x != -1:
            return (start_x, y)


def turn_right(dir):
    x, y = dir
    return (-y, x)


def part1(map):
    current_loc = find_start(map)
    current_dir = (0, -1)

    off_map = False
    locations = set()
    while not off_map:
        off_map, paths, current_loc = find_block(map, current_loc, current_dir)
        locations = locations.union(paths)
        current_dir = turn_right(current_dir)

    return len(locations)


example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

# print(part1(example.split("\n")))
print(part1(utils.get_day_lines(6)))
