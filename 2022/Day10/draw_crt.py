with open("input.txt", "r") as rows:
    current_row = ""
    cycle = 1
    special_cycles = [40, 80, 120, 160, 200, 240]
    pending_add = 0
    x = 1
    while cycle <= 240:
        current_row_pos = (cycle - 1) % 40
        if x - 1 <= current_row_pos and x + 1 >= current_row_pos:
            current_row += "O"
        else:
            current_row += " "
        if pending_add == 0:
            row = rows.readline().strip().split()
            if row[0] == "addx":
                pending_add = int(row[1])
        else:
            x += pending_add
            pending_add = 0
        if cycle in special_cycles:
            print(current_row)
            current_row = ""

        cycle += 1
