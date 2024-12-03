def is_increasing(seq: list[int]):
    return all(n > seq[i-1] for i, n in enumerate(seq[1:], start=1))

def is_decreasing(seq: list[int]):
    return is_increasing(list(reversed(seq)))

def is_monotonic(seq: list[int]):
    return is_increasing(seq) or is_decreasing(seq)

def calculate_distance(a: int, b: int) -> int:
    return abs(a - b)

def is_within_distance_range(seq: list[int], min_: int, max_: int):
    return all(min_ <= calculate_distance(n, seq[i]) <= max_ for i, n in enumerate(seq[:-1], start=1))

class Report:
    def __init__(self, levels: list[int]) -> None:
        self.levels = levels

    def __repr__(self) -> str:
        return f"<Report levels={self.levels}>"

    def is_safe(self) -> bool:
        return is_monotonic(self.levels) and is_within_distance_range(self.levels, 1, 3)
    
with open("2024/day2/input.txt", "r") as file:
    inputs = file.readlines()

safe_reports: list[Report] = []
unsafe_reports: list[Report] = []

for line in inputs:
    report = Report([int(level) for level in line.split()])
    if report.is_safe():
        safe_reports.append(report)
        continue
    unsafe_reports.append(report)

print(f"{len(safe_reports) = }")

made_safe_reports: list[Report] = []

for report in unsafe_reports:
    for i, n in enumerate(report.levels):
        copy = report.levels.copy()
        copy.pop(i)
        if Report(copy).is_safe():
            made_safe_reports.append(report)
            break

print(f"{len(made_safe_reports) = }")

print(f"{len(safe_reports) + len(made_safe_reports) = }")