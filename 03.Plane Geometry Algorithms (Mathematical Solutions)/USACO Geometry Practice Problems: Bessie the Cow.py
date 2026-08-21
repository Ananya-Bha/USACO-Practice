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


""" Several seasons of hot summers and cold winters have taken their toll on Farmer John's fence, and he decides it is time to repaint it, along with the help of his favorite cow, Bessie. Unfortunately, while Bessie is actually remarkably proficient at painting, she is not as good at understanding Farmer John's instructions.

If we regard the fence as a one-dimensional number line, Farmer John paints the interval between x=a and x=b. For example, if a=3 and b=5, then Farmer John paints an interval of length 2. Bessie, misunderstanding Farmer John's instructions, paints the interval from x=c to x=d, which may possibly overlap with part or all of Farmer John's interval. Please determine the total length of fence that is now covered with paint.

INPUT FORMAT (file paint.in):
The first line of the input contains the integers a and b, separated by a space (a<b).

The second line contains integers c and d, separated by a space (c<d).

The values of a, b, c, and d all lie in the range 0…100, inclusive.

OUTPUT FORMAT (file paint.out):
Please output a single line containing the total length of the fence covered with paint.

SAMPLE INPUT:

7 10
4 8

SAMPLE OUTPUT:

6

Here, 6 total units of fence are covered with paint, from x=4 all the way through x=10.  """


painted=
"""7 10
4 8"""

import sys

sys.stdin = open("paint.in","r")
sys.stdout = open("paint.out","w")

painted = sys.stdin.read().splitlines()
a, b = map(int,painted[0].split())
farmer_range=b-a
c, d = map(int,painted[1].split())
cow_range=d-c


overlap = min(b,d)-max(a,c)
if overlap<=0:
    total_area=farmer_range+cow_range
elif overlap>0:
    total_area=(farmer_range+cow_range)-overlap

print(total_area)
    
""" During long milking sessions, Bessie the cow likes to stare out the window of her barn at two huge rectangular billboards across the street advertising "Farmer Alex's Amazingly Appetizing Alfalfa" and "Farmer Greg's Great Grain". Pictures of these two cow feed products on the billboards look much tastier to Bessie than the grass from her farm.

One day, as Bessie is staring out the window, she is alarmed to see a huge rectangular truck parking across the street. The side of the truck has an advertisement for "Farmer Smith's Superb Steaks", which Bessie doesn't quite understand, but she is mostly concerned about the truck potentially blocking the view of her two favorite billboards.

Given the locations of the two billboards and the location of the truck, please calculate the total combined area of both billboards that is still visible. It is possible that the truck obscures neither, both, or only one of the billboards.

INPUT FORMAT (file billboard.in):
The first line of input contains four space-separated integers: x1 y1 x2 y2, where (x1,y1) and (x2,y2) are the coordinates of the lower-left and upper-right corners of the first billboard in Bessie's 2D field of view. The next line contains four more integers, similarly specifying the lower-left and upper-right corners of the second billboard. The third and final line of input contains four integers specifying the lower-left and upper-right corners of the truck. All coordinates are in the range -1000 to +1000. The two billboards are guaranteed not to have any positive area of overlap between themselves.

OUTPUT FORMAT (file billboard.out):
Please output the total combined area of both billboards that remains visible.

SAMPLE INPUT:

1 2 3 5
6 0 10 4
2 1 8 3

SAMPLE OUTPUT:

17

Here, 5 units of area from the first billboard and 12 units of area from the second billboard remain visible.  """


import sys

sys.stdin = open("billboard.in","r")
sys.stdout = open("billboard.out","w")

billboards = sys.stdin.read().splitlines()
B1x1, B1y1, B1x2, B1y2= map(int,billboards[0].split())
B2x1, B2y1, B2x2, B2y2 = map(int,billboards[1].split())
Vx1, Vy1, Vx2, Vy2 = map(int,billboards[2].split())

x_overlap = min(B1x1,Vx2) 
y_overlap = max(B1y1, Vy2)



