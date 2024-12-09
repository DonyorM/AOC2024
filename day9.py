import utils


def parse_input(data: str):
    next_start = 0
    result = []
    block_idx = 0
    char_idx = 0
    while char_idx < len(data):
        val = int(data[char_idx])
        empty = int(data[char_idx + 1]) if char_idx + 1 < len(data) else 0
        result.append((block_idx, next_start, next_start + val))
        next_start += val + empty
        block_idx += 1
        char_idx += 2

    return result


def pack_list(data: list[tuple[int, int, int]]):
    idx = 1
    while idx < len(data):
        _, _, current_end = data[idx - 1]
        _, next_start, _ = data[idx]
        if current_end < next_start:
            remaining_add = next_start - current_end
            end_loc = current_end
            while remaining_add > 0:
                last_idx, last_start, last_end = data[-1]
                last_length = last_end - last_start
                if remaining_add >= last_length:
                    data.pop()
                    data.insert(idx, (last_idx, end_loc, end_loc + last_length))
                    remaining_add -= last_length
                    end_loc += last_length
                    idx += 1
                else:
                    data[-1] = (last_idx, last_start, last_end - remaining_add)
                    data.insert(idx, (last_idx, end_loc, end_loc + remaining_add))
                    remaining_add = 0
        idx += 1


def print_data(data):
    last_end = 0
    for idx, start, end in data:
        if last_end < start:
            print("." * (start - last_end), end="")
        print(str(idx) * (end - start), end="")
        last_end = end
    print()


def score_list(data: list[tuple[int, int, int]]):
    result = 0
    for block_idx, start, end in data:
        for i in range(start, end):
            result += block_idx * i

    return result


def part1(input: str) -> int:
    data = parse_input(input)
    print("Number of blocks: ", len(data))
    pack_list(data)
    print("Packed data, now scoring")
    return score_list(data)


example = "2333133121414131402"
# print(part1(example))
print(part1(utils.get_day_data(9).strip()))
