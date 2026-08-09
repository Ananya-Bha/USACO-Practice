#Synonyms: Brute force, complete search, exhaustative search, cartesian products
#........
#........
#........
#......Q.
#........
#Find the queen on the grid:
grid = ...
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "Q":
            print(f"Found queen at ({x}, {y})!")
#Find all the Xs that is right next to (up, down, left, right) the current X we are looking at
#XX....
#XX....
#....XX
#......
#..X...

#Find all the two combinations of prices that add to get £39.
prices = [12, 18, 21, 27, 30]

for i, x in enumerate(prices):
    for y in prices[i+1:]:
        if x + y == 39:
        print(f"{x} + {y} equals 39.")

#Find all the 2x2 X squares, and print the top-left co-ordinate.
#XX.........
#XX.........
#....XX.....
#.....XX.XX.
#..X.....XX.
#..........X

#XX
#XX

valid = True
dirs = [(0,0), (0,1), (1,0), (1,1)]
for dx, dy in dirs:#Tuple unpacking
    if grid[y+dy][x+dx] != "X":
        valid = False
        break
    


for y, row in enumerate(grid[:-1]):
    for x, square in enumerate(row[:-1]):
        if grid[y][x] == "X" and grid[y][x+1] =="X" and grid[y+1][x] =="X" and grid[y+1][x+1] =="X" :
            print(f"Square found at {x},{y}.")
            
            
for y, row in enumerate(grid[:-1]):
    for x, square in enumerate(row[:-1]):
        if all(grid[y+dy][x+dx] == "X" for dx, dy in [(0,0), (0,1), (1,0), (1,1)]):
            print(f"Square found at {x},{y}.")
                        
