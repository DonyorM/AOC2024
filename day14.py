import re

import utils


def get_robot_position(start_loc, velocity, seconds, grid_width, grid_height):
    return (
        (start_loc[0] + velocity[0] * seconds) % grid_width,
        (start_loc[1] + velocity[1] * seconds) % grid_height,
    )


robot_regex = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")


def parse_robots(text):
    return [
        ((int(g[0]), int(g[1])), (int(g[2]), int(g[3])))
        for g in robot_regex.findall(text)
    ]


def part1(robots, seconds, grid_width, grid_height):
    new_robot_positions = [
        get_robot_position(pos, vel, seconds, grid_width, grid_height)
        for pos, vel in robots
    ]
    top_right = 0
    top_left = 0
    bottom_right = 0
    bottom_left = 0
    for x, y in new_robot_positions:
        if x < grid_width // 2:
            if y < grid_height // 2:
                top_left += 1
            elif y > grid_height // 2:
                bottom_left += 1
        elif x > grid_width // 2:
            if y < grid_height // 2:
                top_right += 1
            elif y > grid_height // 2:
                bottom_right += 1
    return top_left * top_right * bottom_left * bottom_right


def print_map(positions, grid_width, grid_height):
    grid = [["." for _ in range(grid_width)] for _ in range(grid_height)]
    for pos in positions:
        grid[pos[1]][pos[0]] = str(positions[pos])
    for row in grid:
        print("".join([str(x) for x in row]))


def positions_dict(positions, seconds, grid_width, grid_height):
    result = {}
    for pos, vel in positions:
        new_pos = get_robot_position(pos, vel, seconds, grid_width, grid_height)
        if new_pos in result:
            result[new_pos] += 1
        else:
            result[new_pos] = 1
    return result


def find_tree_point(positions: dict[tuple[int, int], int], grid_width, grid_height):
    for pos in positions:
        left = (pos[0] - 1, pos[1] + 1)
        # middle = (pos[0], pos[1] + 1)
        right = (pos[0] + 1, pos[1] + 1)
        left2 = (pos[0] - 2, pos[1] + 2)
        # middle2 = (pos[0], pos[1] + 2)
        right2 = (pos[0] + 2, pos[1] + 2)

        if (
            left in positions
            and left2 in positions
            and right in positions
            and right2 in positions
        ):
            return pos
    return None


# I just keep printing this until I found the right one
def part2(robots, grid_width, grid_height):
    seconds = 2095
    while True:
        positions = positions_dict(robots, seconds, grid_width, grid_height)
        if find_tree_point(positions, grid_width, grid_height):
            print("At second", seconds)
            print_map(positions, grid_width, grid_height)
            print()
            input()
        seconds += 1


example = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

# print(part1(parse_robots(example), 100, 11, 7))
# print(part(parse_robots(utils.get_day_data(14)), 100, 101, 103))
part2(parse_robots(utils.get_day_data(14)), 101, 103)
