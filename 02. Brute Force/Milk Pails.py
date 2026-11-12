import sys
X, Y, M= map(int,sys.stdin.readline().split())
quantity=0
no_of_times_can_fit=M//Y
max_milk=0
for i in range(no_of_times_can_fit+1):
    Total_left=M-(Y*i)
    no_of_x=(Total_left//X)
    total_milk=(Y*i)+(X*no_of_x)
    if total_milk>max_milk:
        max_milk=total_milk

print(max_milk)
