from collections import defaultdict
import utils


DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find_region(grid, char, current_loc, visited_locs):
    current_x, current_y = current_loc
    if grid[current_y][current_x] != char:
        return 0, 0

    visited_locs.add(current_loc)
    perimeter = 0
    area = 1
    for diff in DIRS:
        new_x, new_y = current_x + diff[0], current_y + diff[1]
        if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
            perimeter += 1
            continue

        if grid[new_y][new_x] != char:
            perimeter += 1
            continue

        if (new_x, new_y) in visited_locs:
            continue

        new_perimeter, new_area = find_region(grid, char, (new_x, new_y), visited_locs)
        perimeter += new_perimeter
        area += new_area

    return perimeter, area


def is_side(grid, current_loc, start_diff, sides_counted):
    current_x, current_y = current_loc
    x_change = abs(start_diff[0])
    y_change = abs(start_diff[1])
    diffs = [(y_change, x_change), (-y_change, -x_change)]
    sides_counted_dir = sides_counted[start_diff]
    is_side = True
    sides_counted_dir.add(current_loc)
    for diff in diffs:
        new_x, new_y = current_x + diff[0], current_y + diff[1]
        if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
            continue
        if (
            grid[new_y][new_x] == grid[current_y][current_x]
            and (new_x, new_y) in sides_counted_dir
        ):
            is_side = False
        # sides_counted_dir.add((new_x, new_y))
    return is_side


def is_side_try2(grid, current_loc, start_diff, side_locs):
    start_x, start_y = current_loc
    current_x, current_y = current_loc
    change_x, change_y = start_diff[1], start_diff[0]
    while True:
        new_x, new_y = current_x + change_x, current_y + change_y
        if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
            break

        if grid[new_y][new_x] != grid[start_y][start_x]:
            break

        check_x, check_y = new_x + start_diff[0], new_y + start_diff[1]
        if (
            not (
                check_x < 0
                or check_x >= len(grid[0])
                or check_y < 0
                or check_y >= len(grid)
            )
            and grid[check_y][check_x] == grid[start_y][start_x]
        ):
            break
        current_x, current_y = new_x, new_y

    is_side = (current_x, current_y) not in side_locs
    side_locs.add((current_x, current_y))
    return is_side


def find_region_with_sides(
    grid, char, current_loc, visited_locs: set[tuple[int, int]], sides_counted
):
    current_x, current_y = current_loc
    if grid[current_y][current_x] != char:
        return 0, 0

    visited_locs.add(current_loc)
    sides = 0
    area = 1
    for diff in DIRS:
        new_x, new_y = current_x + diff[0], current_y + diff[1]
        if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
            if is_side_try2(grid, current_loc, diff, sides_counted[diff]):
                sides += 1
            continue

        if grid[new_y][new_x] != char:
            if is_side_try2(grid, current_loc, diff, sides_counted[diff]):
                sides += 1
            continue

        if (new_x, new_y) in visited_locs:
            continue

        new_perimeter, new_area = find_region_with_sides(
            grid, char, (new_x, new_y), visited_locs, sides_counted
        )
        sides += new_perimeter
        area += new_area

    return sides, area


def part1(grid):
    visited_locs = set()
    score = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (x, y) in visited_locs:
                continue
            perimeter, area = find_region(grid, grid[y][x], (x, y), visited_locs)
            score += perimeter * area

    return score


def part2(grid):
    visited_locs = set()
    score = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (x, y) in visited_locs:
                continue

            sides_counted = defaultdict(set)
            sides, area = find_region_with_sides(
                grid, grid[y][x], (x, y), visited_locs, sides_counted
            )
            score += sides * area

    return score


example = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

example2 = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""

example3 = """AAAAAA"""

# print(part2(utils.example_lines(example)))
print(part2(utils.get_day_lines(12)))
