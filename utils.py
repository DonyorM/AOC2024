def get_day_data(day_num):
    with open(f"data/day{day_num}.txt") as f:
        return f.read()


def get_day_lines(day_num):
    with open(f"data/day{day_num}.txt") as f:
        return f.read().splitlines()


def example_lines(example):
    return example.strip().split("\n")
