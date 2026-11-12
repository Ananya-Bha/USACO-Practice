import sys
K, N = map(int,sys.stdin.readline().split())
rankings=[]
for i in range(K):
    session_k=list(map(int,sys.stdin.readline().split()))
    rankings.append(session_k)

no_consistent=0

for cow1 in range(1,N+1):
    for cow2 in range(1,N+1):
        if cow1==cow2:
            continue
        consistent=True
        for session in rankings:
            if session.index(cow1)>session.index(cow2):
                consistent=False
                break

        if consistent:
            no_consistent+=1

print(no_consistent)
