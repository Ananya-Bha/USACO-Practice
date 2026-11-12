import sys
N, D = map(int,sys.stdin.readline().split())
people=list(map(int,sys.stdin.readline().split()))
people_apart=[]
stand_apart=False
for i in range(N):
    stand_apart=True
    for combo in range(N):
        if combo==i:
            continue
        elif abs(people[i]-people[combo])<D :
            stand_apart=False
            break
    if stand_apart==True:
        people_apart.append(i+1)
print(len(people_apart))
print(*people_apart)
