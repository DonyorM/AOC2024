import sys

import utils

POSSIBLE_DIRS = {
    (1, 0): [(1, 0), (0, -1), (0, 1)],
    (-1, 0): [(-1, 0), (0, -1), (0, 1)],
    (0, 1): [(0, 1), (-1, 0), (1, 0)],
    (0, -1): [(0, -1), (-1, 0), (1, 0)],
}


def find_start(grid):
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "S":
                return (x, y)
    return None


def start_branch(
    grid,
    current_loc,
    current_dir,
    score_to_reach_point,
    current_best: int,
    current_score: int,
):
    x, y = current_loc
    if grid[y][x] == "E":
        return current_score

    best = current_best
    for dir in POSSIBLE_DIRS[current_dir]:
        # if (x + dir[0], y + dir[1]) in visited_locs:
        #     continue
        if grid[y + dir[1]][x + dir[0]] == "#":
            continue

        new_score = current_score + 1
        if dir != current_dir:
            new_score += 1000

        target_loc = (x + dir[0], y + dir[1])

        if target_loc in score_to_reach_point and score_to_reach_point[target_loc] <= new_score:
            continue
        else:
            score_to_reach_point[target_loc] = new_score

        if new_score >= best:
            continue

        result = start_branch(
            grid,
            target_loc,
            dir,
            score_to_reach_point,
            best,
            new_score,
        )

        best = min(best, result)

    return best


def part1(grid):
    start = find_start(grid)
    return start_branch(grid, start, (1, 0), {}, sys.maxsize, 0)


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

# print(part1(utils.example_lines(example2)))
print(part1(utils.get_day_lines(16)))
