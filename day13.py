import re

import utils


code_regex = re.compile(
    r"""Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)""",
    re.MULTILINE,
)

A_COST = 3
B_COST = 1


def parse_numbers(text):
    return [[int(x) for x in match] for match in code_regex.findall(text)]


def calculate_cost(input):
    a_x, a_y, b_x, b_y, prize_x, prize_y = input
    b_count = (prize_y * a_x - prize_x * a_y) / (b_y * a_x - b_x * a_y)
    a_count = (prize_x - b_count * b_x) / a_x

    if a_count > 100 or b_count > 100 or a_count % 1 != 0 or b_count % 1 != 0:
        return 0

    return a_count * A_COST + b_count * B_COST


def part1(text):
    return sum(calculate_cost(input) for input in parse_numbers(text))


example = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

# print(part1(example))
print(part1(utils.get_day_data(13)))
