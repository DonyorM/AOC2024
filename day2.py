import utils

EXAMPLE = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
10 16 18 21 24 27
1 3 6 7 3
24 16 18 21 24 27
12 15 9 7 6 5"""


def parse_input():
    lines = utils.get_day_lines(2)
    # lines = utils.example_lines(EXAMPLE)
    return [[int(x) for x in line.split()] for line in lines]


def part1():
    data = parse_input()
    result = 0
    for line in data:
        line_sorted = sorted(line)
        reversed_line_sorted = sorted(line, reverse=True)
        if not (line == line_sorted or line == reversed_line_sorted):
            continue

        for i in range(len(line) - 1):
            diff = abs(line[i] - line[i + 1])
            if not (1 <= diff <= 3):
                break
        else:
            result += 1

    return result


def compare(first, next, ascending):
    diff = abs(next - first)
    if not (1 <= diff <= 3):
        return False
    if ascending and first > next:
        return False
    elif not ascending and first < next:
        return False

    return True


def get_dir_valid(line, ascending):
    i = 0
    skipped = False
    while i < len(line) - 1:
        result = compare(line[i], line[i + 1], ascending)
        if not result:
            if not skipped:
                if i == len(line) - 2:
                    skipped = True
                else:
                    result = compare(line[i], line[i + 2], ascending)
                    if result:
                        skipped = True
                        i += 1
                    else:
                        if i == 0:
                            # Try skipping first element
                            result = compare(line[i + 1], line[i + 2], ascending)
                            if result:
                                skipped = True
                                i += 1
                            else:
                                return False
                        else:
                            return False
            else:
                return False
        i += 1

    return True


def part2():
    data = parse_input()
    result = 0
    with open("output.txt", "w") as f:
        for line in data:
            ascending = get_dir_valid(line, True)
            descending = False
            if not ascending:
                descending = get_dir_valid(line, False)

            if ascending or descending:
                result += 1
            else:
                f.write(f"{' '.join([str(x) for x in line])}\n")

    return result


# Too low: 409
print(part2())
