import sys

import utils

POSSIBLE_DIRS = {
    (1, 0): [(0, -1), (0, 1), (1, 0)],
    (-1, 0): [(0, -1), (0, 1), (-1, 0)],
    (0, 1): [(-1, 0), (1, 0), (0, 1)],
    (0, -1): [(-1, 0), (1, 0), (0, -1)],
}


def find_start(grid):
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "S":
                return (x, y)
    return None


def search_maze(
    grid,
    start_loc,
    start_dir,
):
    to_search = [(start_loc, start_dir, 0)]
    score_to_reach_point = {start_loc: 0}
    current_best = sys.maxsize
    while len(to_search) > 0:
        current_loc, current_dir, current_score = to_search.pop()
        x, y = current_loc
        if grid[y][x] == "E":
            current_best = min(current_score, current_best)
            continue

        for dir in POSSIBLE_DIRS[current_dir]:
            target_loc = (x + dir[0], y + dir[1])
            if grid[target_loc[1]][target_loc[0]] == "#":
                continue

            new_score = current_score + 1
            if dir != current_dir:
                new_score += 1000

            if new_score >= current_best:
                continue

            if target_loc in score_to_reach_point and score_to_reach_point[target_loc] <= new_score:
                continue
            else:
                score_to_reach_point[target_loc] = new_score

            to_search.append((target_loc, dir, new_score))

    return current_best


def part1(grid):
    start = find_start(grid)
    return search_maze(grid, start, (1, 0))


example = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

example2 = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

# print(part1(utils.example_lines(example)))
# 85440 is too high
print(part1(utils.get_day_lines(16)))
