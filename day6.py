from collections import defaultdict
from typing import Mapping
import utils


def print_map(map):
    for line in map:
        print(line)


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


def is_map_loop(map, start_loc, start_dir):
    current_loc = start_loc
    current_dir = start_dir

    paths_for_dir = defaultdict(set)

    off_map = False
    while not off_map:
        off_map, paths, current_loc = find_block(map, current_loc, current_dir)

        paths_for_dir[current_dir] = paths_for_dir[current_dir].union(paths)

        current_dir = turn_right(current_dir)

        if current_loc in paths_for_dir[current_dir]:
            return True
    return False


def find_map_paths(map):
    current_loc = find_start(map)
    current_dir = (0, -1)

    off_map = False
    locations = set()
    while not off_map:
        off_map, paths, current_loc = find_block(map, current_loc, current_dir)
        locations = locations.union(paths)
        current_dir = turn_right(current_dir)

    return locations


def part2(map):
    current_loc = find_start(map)
    current_dir = (0, -1)

    possible_locations = find_map_paths(map)
    total_loops = 0
    i = 0
    for x, y in possible_locations:
        i += 1
        if i % 1000 == 0:
            print(f"{i}/{len(possible_locations)}")
        if map[y][x] == ".":
            new_map = map.copy()
            new_map[y] = new_map[y][:x] + "#" + new_map[y][x + 1 :]
            if is_map_loop(new_map, current_loc, current_dir):
                total_loops += 1

    return total_loops


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

# print(part2(example.split("\n")))
print(part2(utils.get_day_lines(6)))
