#O(log(n)) - the number of steps is related to a log version of n (binary search (needs to be sorted))
numbers = [8, 12, 4, 17, 23]
#Biggest (no nested loop)
max(numbers)
highest = 0
for x in numbers:
    if x > highest: highest = x
#One nested loop (two overall)
#Every pair in a list that adds to 21
for i, x in enumerate(numbers):
    for y in numbers[i+1:]:
        if x+y == 21: 
            print(f"{x} + {y} equals 21")
            
#One loop - O(n) (also Linear Search)
#6 => 3 => 2 => 1
#13 => 7 => 4 => 2 => 1
#250 => 125 => 63 => 32 => 16 => 8 => 4 => 2 => 1
            
rank = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
suit = ["Spades", "Hearts", "Diamonds", "Clubs"]
#Cartesian Product =  when you are creating a new set that combines two options from two sets
for r in rank:
    for s in suit:
        print(r, s)
        
#Two loops - O(n^2) (very bad, also Bubble Sort) (still might need to brute force)
        
numbers = [35, 78, 89, 56, 12, 18, 67, 39, 40, 56, 28, 94, 96, 17, 47, 58, 74, 63, 21, 14, 55, 32]
#Print out all of the two numbers that have a difference of 7
for i, x in enumerate(numbers):
    for y in numbers[i+1:]:
        if (x - y)==7 or (y-x)==7: #abs(x-y) == 7 -> shorter method
            print(f"{x} and {y} subtract to give 7")

#Brute force = no fancy tricks, just checking every possible combination:
#Password cracking
pin = "6813"
for i in range(10000):
    i = str(i)
    pin_code = (4-len(i))*"0"+i
    if pin_code == pin:
https://www.mytutor.co.uk/classroom/launch.html?class=X8T75AAEFK9XHS60ZEKO&tracktutorial=true&pe=LESSONSPACE&p=lessonspace&v=default&device-test=done#        print(f"Found! pin code is {pin}")
        break
    
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


