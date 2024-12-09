from collections import defaultdict
import itertools

import utils


def parse_map(input: list[str]):
    antennas = defaultdict(list)

    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char != ".":
                antennas[char].append((x, y))

    return antennas


def loc_on_map(x, y, max_x, max_y):
    return 0 <= x <= max_x and 0 <= y <= max_y


def get_antinodes(antenna_locs: list[tuple[int, int]], max_x: int, max_y: int):
    combinations = itertools.product(antenna_locs, repeat=2)
    locs = set()
    for (x1, y1), (x2, y2) in combinations:
        if x1 == x2 and y1 == y2:
            continue

        x_diff = x1 - x2
        y_diff = y1 - y2
        loc1 = (x1 + x_diff, y1 + y_diff)
        loc2 = (x2 - x_diff, y2 - y_diff)
        if loc_on_map(*loc1, max_x, max_y):
            locs.add(loc1)
        if loc_on_map(*loc2, max_x, max_y):
            locs.add(loc2)

    return locs


def part1(map):
    antennas = parse_map(map)
    max_y = len(map) - 1
    max_x = len(map[0]) - 1
    antinodes = set()

    for antenna_locs in antennas.values():
        antinodes.update(get_antinodes(antenna_locs, max_x, max_y))

    return len(antinodes)


example = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

# 335 is too high
# print(part1(utils.example_lines(example)))
print(part1(utils.get_day_lines(8)))
