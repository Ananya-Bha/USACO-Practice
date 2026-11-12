import sys
N = int(sys.stdin.readline())
coordinates=[]
for i in range(N):
    pos=list(map(int,sys.stdin.readline().split()))
    coordinates.append(pos)

max_area=0
for i in range(N):
    for j in range(i+1,N):
        for z in range(j+1,N):
            horizontal=False
            if coordinates[i][1]==coordinates[j][1] or coordinates[i][1]==coordinates[z][1] or coordinates[z][1]==coordinates[j][1]:
                horizontal=True
            vertical=False
            if coordinates[i][0]==coordinates[j][0] or coordinates[i][0]==coordinates[z][0] or coordinates[z][0]==coordinates[j][0]:
                vertical=True
            if not vertical or not horizontal:
                continue
            x_max=max(coordinates[i][0],coordinates[j][0],coordinates[z][0])
            x_min=min(coordinates[i][0],coordinates[j][0],coordinates[z][0])
            difference_x=x_max-x_min
            y_max=max(coordinates[i][1],coordinates[j][1],coordinates[z][1])
            y_min=min(coordinates[i][1],coordinates[j][1],coordinates[z][1])
            difference_y=y_max-y_min
            area=difference_x*difference_y
            if area>max_area:
                max_area=area
            
print(max_area)
