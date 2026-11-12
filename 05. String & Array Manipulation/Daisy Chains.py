import sys
N = int(sys.stdin.readline())
flowers=list(map(int,sys.stdin.readline().split()))
no_of_pictures=0
for i in range(N):
    for j in range(i,N):
        combo=flowers[i:j+1]
        average_petal=sum(combo)/len(combo)
        for petals in combo:
            if petals==average_petal:
                no_of_pictures+=1
                break

print(no_of_pictures)
