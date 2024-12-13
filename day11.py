from collections import defaultdict
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


TOTAL_ROUNDS = 75


def stone_blinked_memoized(
    stone: int,
    total_rounds: int,
    start_round: int,
    memo: dict[int, dict[int, list[int]]],
):
    if start_round == total_rounds:
        return stone_blinked(stone)

    if stone in memo:
        memoized_rounds = sorted(memo[stone].keys(), reverse=True)
        to_grab = next(
            (x for x in memoized_rounds if x + start_round <= total_rounds), None
        )
        if to_grab is not None:
            new_stones = memo[stone][to_grab]
            next_round = start_round + to_grab + 1
            if next_round > total_rounds:
                return new_stones
        else:
            new_stones = stone_blinked(stone)
            next_round = start_round + 1
    else:
        new_stones = stone_blinked(stone)
        next_round = start_round + 1

    result = []
    for stone in new_stones:
        result += stone_blinked_memoized(stone, total_rounds, next_round, memo)

    rounds_moved = total_rounds - start_round
    if stone not in memo:
        memo[stone] = {rounds_moved: result}
    else:
        memo[stone][rounds_moved] = result

    print(" " * (3 - start_round), "after round", start_round, "stones", result)
    return result
    # next_round = round + 1
    # new_stones = [stone]
    # if stone in memo:
    #     memoized_rounds = sorted(memo[stone].keys(), reverse=True)
    #     to_grab = next((x for x in memoized_rounds if x + round <= total_rounds), None)
    #     new_stones = memo[stone][to_grab]
    #     next_round = round + to_grab + 1


def parse_line(line: str) -> list[int]:
    return [int(x) for x in line.split()]


def part1(line: str):
    stones = parse_line(line)
    for i in range(25):
        if i % 10 == 0:
            print("Finished round", i)
        new_stones = []
        for stone in stones:
            new_stones += stone_blinked(stone)
        stones = new_stones
    return len(stones)


def get_stones_for_rounds(stones: list[int], rounds: int):
    for i in range(rounds):
        new_stones = []
        for stone in stones:
            new_stones += stone_blinked(stone)
        stones = new_stones
    return stones


def parse_stones(stone: int):
    stones = [stone]
    for i in range(25):
        new_stones = []
        for stone in stones:
            new_stones += stone_blinked(stone)
        stones = new_stones

    return stones


MEMO_SIZE = 15


def parse_stones_memo_fives(stone: int, rounds_left: int, memo: int):
    if rounds_left == 0:
        return [stone]
    if stone in memo and rounds_left in memo[stone]:
        return memo[stone][rounds_left]

    stones = [stone]
    for i in range(MEMO_SIZE):
        new_stones = []
        for s in stones:
            new_stones += stone_blinked(s)
        stones = new_stones
    memo[stone][MEMO_SIZE] = stones

    new_rounds_left = rounds_left - MEMO_SIZE
    new_stones = []
    for s in stones:
        new_stones += parse_stones_memo_fives(s, new_rounds_left, memo)

    if rounds_left != 75:
        # No point in memoizing the last round, it's not duplicated anywhere
        memo[stone][rounds_left] = new_stones
    return new_stones


def part2(line: str):
    total_rounds = 75
    memo_count = 25
    stones = parse_line(line)
    memo = defaultdict(dict)
    final_result = 0
    with ThreadPool(processes=4) as pool:
        for i in range(total_rounds // memo_count):
            search_stones = []
            result_stones = []
            for stone in stones:
                if stone in memo:
                    result_stones += memo[stone]
                else:
                    search_stones.append(stone)
            results = pool.map(
                lambda x: (x, get_stones_for_rounds([x], memo_count)), search_stones
            )
            for stone, result in results:
                memo[stone] = result
                result_stones += result
            stones = result_stones
            print("Finished round", i)
        final_result = len(stones)
    return final_result


# def part2(line: str):
#     stones = parse_line(line)
#     memo = {}
#     memoize_size = 25
#     total_rounds = 6
#     new_stones = []
#     for stone in stones:
#         new_stones += stone_blinked_memoized(stone, total_rounds, 1, memo)

#     print(new_stones)
#     print(len(new_stones))


example = "125 17"

# print(part2(example))
print(part2(utils.get_day_data(11)))
