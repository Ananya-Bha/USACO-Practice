#Write a program that figures out what level the elevator is at
changes = ["UP 3", "DOWN 1", "UP 5", "DOWN 4"]
elevator_floor = 0
for change in changes:
    direction, amount = change.split()
    direction = int(direction)
    if direction == "UP":
        elevator_floor += direction
    elif direction == "DOWN":
        elevator_floor -= direction

print(f"Elevator floor is at {elevator_floor}.")

#Write a program that prints the amount of open lockers after the commands
#There are 10 lockers in total.

changes = ['OPEN 4', 'OPEN 7', 'CLOSE 4', 'OPEN 1']

open_lockers = 0

#min(3, 5) => 3

for change in changes:
    command,number = changes.split()
    number =int(number)
    if command =="OPEN":
        open_lockers = min(open_lockers+number, 10)
        #open_lockers+=number
        #if open_lockers>10:
        #    open_lockers = 10
    elif command =="CLOSE":
        open_lockers = max(open_lockers-number, 0)
        #open_lockers-=number
        #if open_lockers<0:
        #    open_lockers = 0
    
