import re

PATTERN = r"mul\((\d{1,3}),(\d{1,3})\)|(don't\(\))|(do\(\))"

with open("2024/day3/input.txt", "r") as file:
    inputs = file.readlines()

numbers = []
activated = True
x = 0

for line in inputs:
    m = re.findall(PATTERN, line)
    numbers.extend(m)

print(sum(int(a)*int(b) for a, b, c, d in numbers if a and b))

for a, b, c, d in numbers:
    if d == "do()":
        activated = True
        continue

    if c == "don't()":
        activated = False
        continue

    if not activated:
        continue

    x += int(a)*int(b)

print(x)