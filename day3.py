import re

import utils

example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
example2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def day1(input):
    matches = re.findall(r"mul\((\d+),(\d+)\)", input)
    return sum(int(a) * int(b) for a, b in matches)


def day2(input):
    region_start = 0
    result = 0
    while region_start >= 0:
        region, region_start = find_region(region_start, input)
        if region:
            result += day1(region)

    return result


def find_region(start, input: str):
    region_end = input.find("don't()", start)
    next_start = input.find("do()", region_end)
    return input[start:region_end], next_start


print(day2(utils.get_day_data(3)))
