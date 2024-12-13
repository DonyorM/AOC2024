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

# print(part1(utils.example_lines(example)))
print(part1(utils.get_day_lines(12)))
