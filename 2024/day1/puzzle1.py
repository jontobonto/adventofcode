def calculate_distance(a: int, b: int) -> int:
    return abs(a - b)

with open("2024/day1/input.txt", "r") as file:
    lines = file.readlines()

left_loc_ids: list[int] = []
right_loc_ids: list[int] = []

for line in lines:
    left_loc_id, right_loc_id = line.split("   ")
    right_loc_id = right_loc_id.rstrip("\n")

    left_loc_ids.append(int(left_loc_id))
    right_loc_ids.append(int(right_loc_id))

assert len(left_loc_ids) == len(right_loc_ids)

left_loc_ids.sort()
right_loc_ids.sort()

distances = []

for left_loc_id, right_loc_id in zip(left_loc_ids, right_loc_ids):
    distances.append(calculate_distance(left_loc_id, right_loc_id))

print(sum(distances))