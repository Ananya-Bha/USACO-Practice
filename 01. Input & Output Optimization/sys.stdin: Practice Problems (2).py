#------------------------------#
# Alice 16 82
# Bob 17 91    ["Alice 16 82", ] [["Alice", "16", "82"], ]
# Charlie 15 76
# David 16 88
# Eva 17 95
# Input file: list of name, age, and marks
# Read the file, calculate the average mark, print out all the names of the people who got >= 90 marks and are aged 16

import sys
grid = sys.stdin.read().splitlines()
grid2 = [x.split() for x in grid]
total = 0

for row in grid2:
    mark= int(row[2])
    age=int(row[1])
    name=row[0]
    total+=mark
    if mark>=90 and age==16:
        sys.stdin.write(f"High Achiever: {name}")
    
average= total/len(grid2)
sys.stdin.write(f"Average Mark: {average}")
#------------------------------#
# Penzance 9:45
# London 9:15
# Manchester 11:42
# Leeds 13:05
# Portsmouth 10:10
# Edinburgh 8:45
# Cardiff 9:30
# Print out the city with the earliest departure

times = sys.stdin.read().splitlines()
times2d = [x.split() for x in grid]
lowest_hour = 23
lowest_min = 59
lowest_index = -1
hour=[]
minute_times=[]
for row in times2:
    timing = row[1]
    city= row[0]
    hours, minutes = timing.split(":") # Unpacking
    hour.append(hours)
    minute_times.append(minutes)
    
for i in range(len(hour)):
    if hour[i]<lowest_hour: # Check if hour is lower
        lowest_hour=hour[i]
        lowest_min=minute_times[i]
        city=times2d[i][0]
    #Check if hour is the same, but minutes is lower
    elif hour[i]==lowest_hour and lowest_min<minute_times[i]:
        lowest_min = minute_times[i]
        city=times2d[i][0]
        
sys.stdin.write(f"City with the earliest departure time is .... {city}")

#------------------------------------------------------------#
# ........
# ...Q....
# ........
# ........
# .....K..
# ........
# .P......
# ........
#Chess board - Print out the coordinates of all the remaining pieces
    
chess = sys.stdin.read().splitlines()
for y, row in enumerate(chess):
    for x, piece in enumerate(row):
        if piece!=".":
            sys.stdin.write(f"{piece} at {x},{y}")
