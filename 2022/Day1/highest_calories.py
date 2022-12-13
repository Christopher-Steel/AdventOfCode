max_found = 0
current_elf_total = 0

with open("./calorie_counts.txt", "r") as rows:
    for row in rows.readlines():
        row = row.strip()
        if row == "":
            max_found = max(max_found, current_elf_total)
            current_elf_total = 0
        else:
            current_elf_total += int(row)

print("Max elf calories: ", max_found)
