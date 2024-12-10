import utils


DIR_DIFFS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def score_location(
    scores: dict[tuple[int, int], set[tuple[int, int]]],
    map: list[list[int]],
    loc: tuple[int, int],
) -> set[tuple[int, int]]:
    score = set()
    current_x, current_y = loc

    if map[current_y][current_x] == 9:
        scores[loc] = score
        score.add(loc)
        return score

    for diff in DIR_DIFFS:
        new_x, new_y = current_x + diff[0], current_y + diff[1]
        if new_x < 0 or new_x >= len(map[0]) or new_y < 0 or new_y >= len(map):
            continue

        if map[new_y][new_x] - map[current_y][current_x] != 1:
            continue

        if (new_x, new_y) in scores:
            score.update(scores[(new_x, new_y)])
        else:
            score.update(score_location(scores, map, (new_x, new_y)))

    scores[loc] = score
    return score


def parse_map(lines: list[str]) -> list[list[int]]:
    return [[int(x) for x in line] for line in lines]


def part1(lines: list[str]):
    map = parse_map(lines)
    scores = {}
    total_score = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                reachable_ends = score_location(scores, map, (x, y))
                total_score += len(reachable_ends)

    return total_score


def rate_location(
    ratings: dict[tuple[int, int], set[int]],
    map: list[list[int]],
    loc: tuple[int, int],
) -> int:
    rating = 0
    current_x, current_y = loc

    if map[current_y][current_x] == 9:
        ratings[loc] = 1
        return 1

    for diff in DIR_DIFFS:
        new_x, new_y = current_x + diff[0], current_y + diff[1]
        if new_x < 0 or new_x >= len(map[0]) or new_y < 0 or new_y >= len(map):
            continue

        if map[new_y][new_x] - map[current_y][current_x] != 1:
            continue

        if (new_x, new_y) in ratings:
            rating += ratings[(new_x, new_y)]
        else:
            rating += rate_location(ratings, map, (new_x, new_y))

    ratings[loc] = rating
    return rating


def part2(lines: list[str]):
    map = parse_map(lines)
    ratings = {}
    total_score = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                total_score += rate_location(ratings, map, (x, y))

    return total_score


example = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

# print(part2(utils.example_lines(example)))
print(part2(utils.get_day_lines(10)))
