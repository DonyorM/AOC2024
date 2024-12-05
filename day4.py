import utils


example = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def find_xmas(input, start_x, start_y, diff_x, diff_y):
    for idx, c in enumerate("XMAS"):
        y_idx = start_y + idx * diff_y
        x_idx = start_x + idx * diff_x
        if y_idx >= len(input) or y_idx < 0 or x_idx >= len(input[y_idx]) or x_idx < 0:
            return 0
        if c != input[y_idx][x_idx]:
            return 0

    return 1


def part1(input):
    count = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == "X":
                count += sum(
                    [
                        find_xmas(input, x, y, 1, 0),  # right
                        find_xmas(input, x, y, -1, 0),  # left
                        find_xmas(input, x, y, 0, 1),  # down
                        find_xmas(input, x, y, 0, -1),  # up
                        find_xmas(input, x, y, 1, 1),  # down right
                        find_xmas(input, x, y, -1, 1),  # down left
                        find_xmas(input, x, y, 1, -1),  # up right
                        find_xmas(input, x, y, -1, -1),
                    ]
                )
    return count


def find_x_mas(input, start_x, start_y, dir_diff):
    s_x = start_x + (2 * dir_diff)
    bottom_y = start_y + 2
    a_y = start_y + 1
    a_x = start_x + dir_diff

    if bottom_y >= len(input) or s_x >= len(input[bottom_y]) or s_x < 0:
        return 0

    if (
        input[start_y][start_x] == "M"
        and input[bottom_y][start_x] == "M"
        and input[a_y][a_x] == "A"
        and input[start_y][s_x] == "S"
        and input[bottom_y][s_x] == "S"
    ):
        return 1

    return 0


def find_x_mas_rotated(input, start_x, start_y, dir_diff):
    s_y = start_y + (2 * dir_diff)
    right_x = start_x + 2
    a_y = start_y + dir_diff
    a_x = start_x + 1

    if right_x >= len(input[start_y]) or s_y >= len(input) or s_y < 0:
        return 0

    if (
        input[start_y][start_x] == "M"
        and input[start_y][right_x] == "M"
        and input[a_y][a_x] == "A"
        and input[s_y][start_x] == "S"
        and input[s_y][right_x] == "S"
    ):
        return 1

    return 0


def part2(input):
    count = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == "M":
                count += find_x_mas(input, x, y, 1)
                count += find_x_mas(input, x, y, -1)
                count += find_x_mas_rotated(input, x, y, 1)
                count += find_x_mas_rotated(input, x, y, -1)
    return count


# print(part2(utils.example_lines(example)))
print(part2(utils.get_day_lines(4)))
