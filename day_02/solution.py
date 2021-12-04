import csv

def yield_movement():
    with open("input.txt") as fh:
        for line in csv.reader(fh, delimiter=" "):
            yield line[0], int(line[1])

def part_1():
    pos_horizontal = 0
    pos_depth = 0
    for direction, quantity in yield_movement():
        if direction == "forward":
            pos_horizontal += int(quantity)
        elif direction == "down":
            pos_depth += int(quantity)
        elif direction == "up":
            pos_depth -= int(quantity)
    return pos_horizontal * pos_depth

def part_2():
    pos_horizontal = 0
    pos_depth = 0
    aim = 0
    for direction, quantity in yield_movement():
        if direction == "forward":
            pos_horizontal += int(quantity)
            pos_depth += (aim * quantity)
        elif direction == "down":
            aim += int(quantity)
        elif direction == "up":
            aim -= int(quantity)
    return pos_horizontal * pos_depth

print(f"Part 1 = {part_1()}")
print(f"Part 2 = {part_2()}")
