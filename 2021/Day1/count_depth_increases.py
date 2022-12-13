previous_depth = None
depth_increases = 0
with open("sonar_readings.txt", "r") as rows:
    for row in rows.readlines():
        row = row.strip()
        if not row:
            continue
        depth = int(row)
        if previous_depth is not None and depth > previous_depth:
            depth_increases += 1
        previous_depth = depth

print(f"Times that depth increased: {depth_increases}")
