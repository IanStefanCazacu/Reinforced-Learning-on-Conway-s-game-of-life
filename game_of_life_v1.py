from collections import Counter
#72
crt_live_cells = {(1,0), (2,0),(0,1), (1,1),(1,2)} #aici o sa fac sa il putem pune manual + ceva interfata, dar momentan asa ramane

def get_neighbors(cell):
    x, y = cell
    return [(x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx, dy) != (0, 0)]

def next_generation(crt_live_cells):
    neighbor_cont = Counter()
    
    for cell in crt_live_cells:
        for neighbor in get_neighbors(cell):
            neighbor_cont[neighbor] += 1
    
    new_live_cells = set()
    
    for cell, cont in neighbor_cont.items():
        if cont == 3 or (cont == 2 and cell in crt_live_cells):
            new_live_cells.add(cell)
    
    return new_live_cells

gen_cont = 0

def print_full_grid(live_cells):
    if not live_cells:
        print("No live cells.")
        return
    
    min_x = min(x for x, y in live_cells)
    max_x = max(x for x, y in live_cells)
    min_y = min(y for x, y in live_cells)
    max_y = max(y for x, y in live_cells)
    
    for y in range(min_y, max_y + 1):
        row = ''
        for x in range(min_x, max_x + 1):
            if (x, y) in live_cells:
                row += 'O '
            else:
                row += '. '
        print(row)
    print()

while True:
    print(f"Generation {gen_cont}: {crt_live_cells}")
    print_full_grid(crt_live_cells)
    ipt = input("1: Next Generation, 2: Exit")
    if ipt == '1':
        crt_live_cells = next_generation(crt_live_cells)
        gen_cont += 1
    elif ipt == '2':
        break
    else:
        print("Invalid input, please enter 1 or 2.")