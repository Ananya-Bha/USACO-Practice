"""

LEAVE 5
ENTER 5
ENTER 12
LEAVE 8"""
#List of car park entries
#Figure out how many are in the car park by the end
#20 spaces in the car park
#Print how many cars were rejected at a a given

total_cars = 0
for change in changes:
    command, number = changes.split()
    number = int(number)
    if command =="ENTER":
        total_cars+=number
        if total_cars>20:
            print("Not enough parking spaces..")
            cars_rejected= total_cars-20
            print(f"{cars_rejected} cars rejected...")
            total_cars-=cars_rejected
            
    if command =="LEAVE":
        total_cars-=number
