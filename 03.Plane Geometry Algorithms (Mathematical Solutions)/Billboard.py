import sys
coordinates = sys.stdin.read().splitlines()
Billboard1= [int(x) for x in coordinates[0].split()]
Billboard2= [int(x) for x in coordinates[1].split()]
truck= [int(x) for x in coordinates[2].split()]
x1, y1 = max(Billboard1[0],truck[0]),max(Billboard1[1],truck[1])
x2, y2 = min(Billboard1[2],truck[2]), min(Billboard1[3],truck[3])
print(x1,y1,x2,y2)
