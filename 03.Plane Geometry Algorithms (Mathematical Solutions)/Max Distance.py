import sys

coordinates = sys.stdin.read().splitlines()
N = int(coordinates[0])
X_coordinates= [int(x) for x in coordinates[1].split()]
Y_coordinates = [int(x) for x in coordinates[2].split()]

max_distance=0
for i in range(N): #if i = n-1, then i+1=n is out of bounds
    for j in range(N):
        x1= X_coordinates[i]
        x2= X_coordinates[j]
        y1= Y_coordinates[i]
        y2= Y_coordinates[j]
        distance = ((x2-x1)**2) + ((y2-y1)**2)
        if distance>max_distance:
            max_distance=distance
    

print(max_distance)
