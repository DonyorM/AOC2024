import utils


def parse_input(lines):
    grid = []
    idx = 0
    while lines[idx].strip() != "":
        grid.append(list(lines[idx].strip()))
        idx += 1

    idx += 1

    return grid, "".join(lines[idx:])


def can_move(grid, loc, dir):
    next_x, next_y = loc[0] + dir[0], loc[1] + dir[1]
    if grid[next_y][next_x] == "#":
        return False
    elif grid[next_y][next_x] == ".":
        return (next_x, next_y)
    else:
        return can_move(grid, (next_x, next_y), dir)


def move_robot(grid, start_loc, dir):
    move_end = can_move(grid, start_loc, dir)
    if move_end:
        current_x, current_y = move_end
        while (current_x, current_y) != start_loc:
            grid[current_y][current_x] = grid[current_y - dir[1]][current_x - dir[0]]
            current_x -= dir[0]
            current_y -= dir[1]

        grid[start_loc[1]][start_loc[0]] = "."
        return (start_loc[0] + dir[0], start_loc[1] + dir[1])
    else:
        return start_loc


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
            if grid[y][x] == "O":
                score += y * 100 + x

    return score


def print_map(grid):
    for row in grid:
        print("".join(row))


def part1(lines):
    grid, movement = parse_input(lines)
    current_loc = find_start_loc(grid)
    for movement_val in movement:
        current_loc = move_robot(grid, current_loc, movement_to_dir(movement_val))
    # print_map(grid)
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

# print(part1(utils.example_lines(example2)))
print(part1(utils.get_day_lines(15)))
