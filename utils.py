import time


def get_day_data(day_num):
    with open(f"data/day{day_num}.txt") as f:
        return f.read()


def get_day_lines(day_num):
    with open(f"data/day{day_num}.txt") as f:
        return f.read().splitlines()


def example_lines(example):
    return example.strip().split("\n")


def timed_run(func, *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    print(f"Time: {end - start:.3f}")
    print(f"Result: {result}")
