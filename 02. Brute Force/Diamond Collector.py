import sys
N, K = map(int,sys.stdin.readline().split())
sizes=[]
for i in range(N):
    diamond_size=int(input())
    sizes.append(diamond_size)

amount=0
for i in range(N):
    ans=0
    min_size=sizes[i] #sizes[i] is the chosen smallest diamond
    max_size=min_size+K # given the smallest diamon, we find the largest size

    #goal: find the # of diamonds that are between min and max
    for j in range(N):
        if (sizes[j]<=max_size) and (sizes[j]>=min_size):
            ans+=1
    if ans>amount:
        amount=ans

print(amount)
