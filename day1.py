import utils


def frequencies(data):
    freqs = {}
    for item in data:
        if item in freqs:
            freqs[item] += 1
        else:
            freqs[item] = 1

    return freqs


def parse_data():
    data = utils.get_day_lines(1)
    first_col = []
    second_col = []
    for line in data:
        first, second = line.split()
        first_col.append(int(first))
        second_col.append(int(second))

    return first_col, second_col


def part1():
    first, second = parse_data()
    first.sort()
    second.sort()
    result = 0
    for i in range(len(first)):
        result += abs(first[i] - second[i])

    return result


def part2():
    first, second = parse_data()
    freqs = frequencies(second)
    return sum([x * freqs[x] for x in first if x in freqs])


print(part2())
