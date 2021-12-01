import csv


def yield_reading():
    with open("input.csv") as f:
        for (reading, ) in csv.reader(f):
            yield int(reading)


def part_1():
    increase_count = 0
    prev_reading = None
    for reading in yield_reading():
        if prev_reading is not None and reading > prev_reading:
            increase_count += 1
        prev_reading = reading
    return increase_count


def part_2():
    increase_count = 0
    rolling_window = []
    prev_rolling_window_sum = None
    for reading in yield_reading():
        reading = int(reading)
        rolling_window.append(reading)
        if len(rolling_window) == 3:
            rolling_window_sum = sum(rolling_window)
            if prev_rolling_window_sum is not None and rolling_window_sum > prev_rolling_window_sum:
                increase_count += 1
            prev_rolling_window_sum = rolling_window_sum
            rolling_window = rolling_window[1:]
    return increase_count


print(f"Part 1 = {part_1()}")
print(f"Part 2 = {part_2()}")
