import utils


def parse_input(lines):
    grid = []
    idx = 0
    while lines[idx].strip() != "":
        line = []
        for val in lines[idx].strip():
            if val == "@":
                line.append("@")
                line.append(".")
            elif val == "O":
                line.append("[")
                line.append("]")
            else:
                line.append(val)
                line.append(val)
        grid.append(line)
        idx += 1

    idx += 1

    return grid, "".join(lines[idx:])


def move_stuff_left_right(grid, start_loc, x_diff):
    current_x, current_y = start_loc
    target_x, target_y = current_x + x_diff, current_y
    if grid[target_y][target_x] == "#":
        return False
    elif grid[target_y][target_x] != ".":
        if not move_stuff_left_right(grid, (target_x, target_y), x_diff):
            return False

    grid[target_y][target_x] = grid[current_y][current_x]
    grid[current_y][current_x] = "."
    return (start_loc[0] + x_diff, start_loc[1])


def find_moveable_locations_up_down(grid, start_loc, y_diff):
    current_x, current_y = start_loc
    moveable_locs = set([start_loc])
    target_x, target_y = current_x, current_y + y_diff
    if grid[target_y][target_x] == "#":
        return False
    elif grid[target_y][target_x] == "[":
        left_result = find_moveable_locations_up_down(
            grid, (target_x, target_y), y_diff
        )
        right_result = find_moveable_locations_up_down(
            grid, (target_x + 1, target_y), y_diff
        )
        if left_result and right_result:
            moveable_locs.update(left_result)
            moveable_locs.update(right_result)
        else:
            return False
    elif grid[target_y][target_x] == "]":
        left_result = find_moveable_locations_up_down(
            grid, (target_x - 1, target_y), y_diff
        )
        right_result = find_moveable_locations_up_down(
            grid, (target_x, target_y), y_diff
        )
        if left_result and right_result:
            moveable_locs.update(left_result)
            moveable_locs.update(right_result)
        else:
            return False

    return moveable_locs


def move_stuff_up_down(grid, start_loc, y_diff):
    moveable_locations = find_moveable_locations_up_down(grid, start_loc, y_diff)
    if moveable_locations:
        moveable_locations = sorted(
            moveable_locations, key=lambda loc: loc[1] * -y_diff
        )
        for loc in moveable_locations:
            current_x, current_y = loc
            grid[current_y + y_diff][current_x] = grid[current_y][current_x]
            grid[current_y][current_x] = "."
        return (start_loc[0], start_loc[1] + y_diff)
    else:
        return False


def move_robot(grid, start_loc, dir):
    if dir[0] != 0:
        result = move_stuff_left_right(grid, start_loc, dir[0])
    else:
        result = move_stuff_up_down(grid, start_loc, dir[1])

    return result or start_loc


def movement_to_dir(movement):
    if movement == "^":
        return (0, -1)
    elif movement == ">":
        return (1, 0)
    elif movement == "v":
        return (0, 1)
    elif movement == "<":
        return (-1, 0)
    else:
        raise ValueError("Invalid movement" + movement)


def find_start_loc(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "@":
                return (x, y)


def score_grid(grid):
    score = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "[":
                score += y * 100 + x

    return score


def print_map(grid):
    for row in grid:
        print("".join(row))


def part2(lines, print_steps_start=False):
    grid, movement = parse_input(lines)
    current_loc = find_start_loc(grid)
    for i, movement_val in enumerate(movement):
        if print_steps_start and i >= print_steps_start:
            print("After step", i)
            print_map(grid)
            print("About to move", movement_val)
            input()
        current_loc = move_robot(grid, current_loc, movement_to_dir(movement_val))

    print_map(grid)
    return score_grid(grid)


example = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

example2 = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

example3 = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""

# print(part2(utils.example_lines(example2), 0))
print(part2(utils.get_day_lines(15)))
