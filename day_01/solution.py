import csv

with open("input.csv") as f:
    increase_count = 0
    prev_reading = None
    for (reading, ) in csv.reader(f):
        reading = int(reading)
        if prev_reading is not None and reading > prev_reading:
            increase_count += 1
        prev_reading = reading

print(increase_count)
