import sys
N = int(sys.stdin.readline())    
S = sys.stdin.readline().strip()    
T = sys.stdin.readline().strip()    

matches=True
for i in range(N):
    if T[i]!="*" and T[i]!=S[i]:
        matches=False
        break

if matches:
    print("Yes")
else:
    print("No")
