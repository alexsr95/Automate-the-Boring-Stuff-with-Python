grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Loop through each row of the final image, which is from top (y=0) to bottom (y=5)
for y in range(6):  # 6 rows total
    # For each row, loop across each column from left (x=0) to right (x=8)
    for x in range(9):  # 9 columns total
        # Print the character at position (x, y) without moving to a new line
        print(grid[x][y], end='')
    # After finishing one row, move to the next line
    print()