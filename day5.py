from collections import defaultdict
import math

import utils


def parse_input(lines: list[str]):
    splitIdx = lines.index("")
    orders = defaultdict(set)
    for line in lines[:splitIdx]:
        first, after = line.split("|")
        orders[first].add(after)

    pages = [line.split(",") for line in lines[splitIdx + 1 :]]

    return orders, pages


def printing_is_valid(orders: dict[str, set[str]], page: list[str]):

    page_order = {val: idx for idx, val in enumerate(page)}

    for val in page:
        if val in orders:
            for after in orders[val]:
                if after in page_order and page_order[after] < page_order[val]:
                    return False

    return True


def part1(lines):
    orders, pages = parse_input(lines)

    result = 0
    for page in pages:
        if printing_is_valid(orders, page):
            middle_idx = math.floor(len(page) / 2)
            result += int(page[middle_idx])

    return result


def sort_page(orders: dict[str, set[str]], page: list[str]):
    not_sorted = True
    while not_sorted:
        for val in page:
            if val in orders:
                val_idx = page.index(val)
                invalid_afters = [
                    after
                    for after in orders[val]
                    if after in page and page.index(after) < val_idx
                ]
                if len(invalid_afters) > 0:
                    min_after = min([page.index(after) for after in invalid_afters])
                    page.pop(val_idx)
                    page.insert(min_after, val)
                    break
        else:
            not_sorted = False


def part2(lines):
    orders, pages = parse_input(lines)

    invalid_pages = [page for page in pages if not printing_is_valid(orders, page)]
    result = 0
    for page in invalid_pages:
        sort_page(orders, page)
        middle_idx = math.floor(len(page) / 2)
        result += int(page[middle_idx])

    return result


example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

# print(part2(utils.example_lines(example)))
print(part2(utils.get_day_lines(5)))
