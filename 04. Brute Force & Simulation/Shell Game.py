import sys
N = int(sys.stdin.readline())
swaps =[]
for i in range(N):
    to_add= list(map(int,sys.stdin.readline().split()))
    swaps.append(to_add)


max_score=0
for position in range(1, 4): #starting pebble position
    #position is START position, but we need to simulate the game 
    score=0
    for i in range(N):
        a=swaps[i][0]
        b=swaps[i][1]
        if position == a:
            position = b
        elif position==b:
            position=a
            
        if position == swaps[i][2]:
            score+=1
    if score > max_score:
        max_score=score

print(max_score)
