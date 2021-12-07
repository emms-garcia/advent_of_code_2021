from collections import defaultdict


class CoordinateCounter(object):
    def __init__(self):
        self.counters = defaultdict(int)
        self.overlaps = 0

    def count(self, coordinate):
        self.counters[coordinate] += 1
        if self.counters[coordinate] == 2:
            self.overlaps += 1


def yield_line_coordinates():
    with open("input.txt") as fh:
        for line in fh.read().split("\n"):
            [start_str, end_str] = line.split(" -> ")
            start, end = start_str.split(","), end_str.split(",")
            yield [int(n) for n in start], [int(n) for n in end]


def part_1():
    counter = CoordinateCounter()
    for start, end in yield_line_coordinates():
        [x1, y1] = start
        [x2, y2] = end
        if x1 == x2:
            ymin, ymax = (y2, y1 + 1) if y1 > y2 else (y1, y2 + 1)
            for y in range(ymin, ymax):
                counter.count((x1, y))
        elif y1 == y2:
            xmin, xmax = (x2, x1 + 1) if x1 > x2 else (x1, x2 + 1)
            for x in range(xmin, xmax):
                counter.count((x, y1))
    return counter.overlaps


def part_2():
    counter = CoordinateCounter()
    for start, end in yield_line_coordinates():
        [x1, y1] = start
        [x2, y2] = end
        if x1 == x2:
            ymin, ymax = (y2, y1 + 1) if y1 > y2 else (y1, y2 + 1)
            for y in range(ymin, ymax):
                counter.count((x1, y))
        elif y1 == y2:
            xmin, xmax = (x2, x1 + 1) if x1 > x2 else (x1, x2 + 1)
            for x in range(xmin, xmax):
                counter.count((x, y1))
        else:
            x, y = x1, y1
            counter.count((x, y))
            while x != x2 and y != y2:
                if x != x2:
                    x += 1 if (x2 > x) else -1
                if y != y2:
                    y += 1 if (y2 > y) else -1
                counter.count((x, y))
    return counter.overlaps


print(f"Part 1 = {part_1()}")
print(f"Part 2 = {part_2()}")
