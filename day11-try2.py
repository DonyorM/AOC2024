from multiprocessing.pool import ThreadPool

import utils


def stone_blinked(stone: int):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        first_half = str(stone)[: len(str(stone)) // 2]
        second_half = str(stone)[len(str(stone)) // 2 :]
        return [int(first_half), int(second_half)]
    else:
        return [stone * 2024]


def count_stone(stone: int, current_round, max_rounds, memo):
    if current_round == max_rounds:
        return 1

    if (stone, current_round) in memo:
        return memo[(stone, current_round)]

    new_stones = stone_blinked(stone)
    result = sum(
        count_stone(stone, current_round + 1, max_rounds, memo) for stone in new_stones
    )

    memo[(stone, current_round)] = result
    return result


def part2(line: str):
    total_rounds = 25
    stones = parse_line(line)
    memo = {}
    # with ThreadPool(processes=8) as pool:
    #     result = pool.map(lambda stone: count_stone(stone, 0, total_rounds), stones)
    result = [count_stone(stone, 0, total_rounds, memo) for stone in stones]

    return sum(result)


def parse_line(line: str) -> list[int]:
    return [int(x) for x in line.split()]


print(part2(utils.get_day_data(11)))
