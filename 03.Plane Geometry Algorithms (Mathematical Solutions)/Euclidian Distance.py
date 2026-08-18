#Find the euclidean distance

p1 = (3,2)
p2 = (0,-3)

def dist(p1, p2):
    x1, y1 = p1 #Tuple unpacking
    x2, y2 = p2 #Tuple unpacking
    distance = ((x2-x1)^2+(y2-y1)^2)^0.5
    print(f"Distance between {x1,y1} and {x2,y2} is {distance}..")
    
rect1 = [(0,-3), (3,2)]
rect2 = [(2,1), (7,3)]
#Is there an overlap?
#Check if horizontal spread of one rectangle is overlapping another rectangle?
#Check if vertical spread of one rectangle is overlapping another rectangle?
