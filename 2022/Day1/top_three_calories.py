elf_totals_found = []
current_elf_total = 0

with open("./calorie_counts.txt", "r") as rows:
    for row in rows.readlines():
        row = row.strip()
        if row == "":
            elf_totals_found.append(current_elf_total)
            current_elf_total = 0
        else:
            current_elf_total += int(row)

total_top_three = sum(sorted(elf_totals_found, reverse=True)[0:3])

print("Total of top three elf calories: ", total_top_three)
