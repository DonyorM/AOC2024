import utils


def is_row_possible(total: int, next_num: int, rest_nums: list[int]) -> bool:
    if next_num > total:
        return False
    if len(rest_nums) == 0:
        return next_num == total

    operate_num = rest_nums[0]
    rest_nums = rest_nums[1:]
    if is_row_possible(total, next_num + operate_num, rest_nums):
        return True
    return is_row_possible(total, next_num * operate_num, rest_nums)


def parse_input(lines: list[str]):
    result = []
    for line in lines:
        total, rest = line.split(": ")
        result.append((int(total), [int(x) for x in rest.split()]))
    return result


def part1(input: list[str]) -> int:
    rows = parse_input(input)
    return sum(
        [total for total, rest in rows if is_row_possible(total, rest[0], rest[1:])]
    )


example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

print(part1(utils.get_day_lines(7)))
