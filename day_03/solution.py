from collections import defaultdict


def yield_reading():
    with open("input.txt") as fh:
        for line in fh:
            yield line.strip()


def part_1():
    counters = defaultdict(lambda: defaultdict(int))
    for reading in yield_reading():
        for i, bit in enumerate(reading):
            counters[i][bit] += 1

    gama_rate = ""
    epsilon_rate = ""
    for i in range(len(counters)):
        if counters[i]["0"] > counters[i]["1"]:
            gama_rate += "1"
            epsilon_rate += "0"
        else:
            gama_rate += "0"
            epsilon_rate += "1"
    return int(gama_rate, 2) * int(epsilon_rate, 2)


def _group_rows_by_bit(col_idx, bit_matrix, remaining_rows):
    counters = {"0": set(), "1": set()}
    for row_idx in remaining_rows:
        counters[bit_matrix[row_idx][col_idx]].add(row_idx)
    return counters


def part_2():
    bit_matrix = [reading for reading in yield_reading()]
    col_idx = 0
    remaining_rows_co2 = set(range(len(bit_matrix)))
    remaining_rows_o2 = set(range(len(bit_matrix)))
    while len(remaining_rows_co2) > 1 or len(remaining_rows_o2) > 1:
        if len(remaining_rows_co2) > 1:
            rows_by_bit = _group_rows_by_bit(col_idx, bit_matrix, remaining_rows_co2)
            most_common_bit = "1" if len(rows_by_bit["1"]) < len(rows_by_bit["0"]) else "0"
            remaining_rows_co2 = rows_by_bit[most_common_bit]
        if len(remaining_rows_o2) > 1:
            rows_by_bit = _group_rows_by_bit(col_idx, bit_matrix, remaining_rows_o2)
            least_common_bit = "1" if len(rows_by_bit["1"]) >= len(rows_by_bit["0"]) else "0"
            remaining_rows_o2 = rows_by_bit[least_common_bit]
        col_idx += 1

    co2_rating = int(bit_matrix[remaining_rows_co2.pop()], 2)
    o2_rating = int(bit_matrix[remaining_rows_o2.pop()], 2)
    return co2_rating * o2_rating


print(f"Part 1 = {part_1()}")
print(f"Part 2 = {part_2()}")
