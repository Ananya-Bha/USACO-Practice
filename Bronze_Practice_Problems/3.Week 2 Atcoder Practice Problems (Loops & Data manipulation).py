#WEEK 2 PRACTICE PROBLEMS

#A : First ABC 2
'''
import sys
N= int(sys.stdin.readline())
S= sys.stdin.readline().strip()

index_pos=0
found=False
substring=""
for i in range(N-2):
    substring=S[i:i+3]
    if substring == "ABC":
        index_pos=i
        found=True
        break

if found:
    print(index_pos+1)
else:
    print(-1)
'''

#B - Everyone is Friends
'''
import sys
N, M= map(int,sys.stdin.readline().split())
grid = [[0] * 100 for _ in range(100)]
for i in range(M):
    party_i=list(map(int,sys.stdin.readline().split()))
    for index,person in enumerate(party_i):
        if index!=0:
            grid[i][person-1]=1

attended_all=True
for i in range(N):
    for j in range(N):
        found=False
        for party in range(M):
            if grid[party][i] ==1 and grid[party][j]==1:
                found=True
        if found==False:
            attended_all=False

if attended_all==True:
    print("Yes")
else:
    print("No")
'''

#B - Strawberries
'''
import sys
N, K = map(int,sys.stdin.readline().split())
S = list(sys.stdin.readline().strip())
char_list=[]
for i in range(N):
    if S[i]=="O":
        char_list.append(0)
    else:
        char_list.append(1)
        
can_eat=0
for tooth in range(N):
    check_tooth=True
    if tooth+K-1<N:
        for char in range(K):
            if char_list[tooth+char] == 1:
                check_tooth=False
    else:
        check_tooth=False
    if check_tooth==True:
        can_eat+=1
        for char in range(K):
            char_list[tooth+char]=1

print(can_eat)
'''

#B - Vacation Together
#1 -> busy O-> free
'''
import sys
N, D = map(int,sys.stdin.readline().split())
grid = grid = [[0] * D for _ in range(N)]
for person in range(N):
    person_i=list(sys.stdin.readline().strip())
    for index, day in enumerate(person_i):
        if day=="o":
            grid[person][index]=0
        else:
            grid[person][index]=1

consecutive_days=0
max_days=0
for day in range(D):
    all_free=True
    for person in range(N):
        if grid[person][day]==1:
            all_free=False
            
    if all_free:
        consecutive_days+=1
        max_days=max(max_days,consecutive_days)
    else:
        consecutive_days=0

print(max_days)
'''

#B - 326-like Numbers
'''
import sys
N = int(sys.stdin.readline())


number=N
while number>=N:
    digits=[]
    temp_no=number
    while temp_no>0:
        last_digit=temp_no%10
        digits.append(last_digit)
        temp_no=temp_no//10

    if digits[2]*digits[1]==digits[0]:
        print(number)
        break
    else:
        number+=1
'''

#A - Beautful Year
'''
import sys
Y=int(sys.stdin.readline())

year=Y+1
while year>Y:
    digits=[]
    temp_yr=year
    while temp_yr>0:
        last_digit=temp_yr%10
        digits.append(last_digit)
        temp_yr=temp_yr//10

    equal=False
    for i in range(len(digits)):
        for j in range(i+1,len(digits)):
            if digits[i]==digits[j]:
                equal=True
    if not equal:
        print(year)
        break
    else:
        year+=1
'''

#B - Farthest Point
''''
import sys
N = int(sys.stdin.readline())
coordinates=[]
for coordinate in range(N):
    x,y=map(int,sys.stdin.readline().split())
    coordinates.append([x,y])

for i in range(N):
    max_distance=-1
    farthest_point=0
    x1,y1=coordinates[i]
    for j in range(N):
        x2,y2=coordinates[j]

        distance=((x1-x2)**2 + (y1-y2)**2)**0.5
        if distance>max_distance:
            max_distance=distance
            farthest_point=j

    print(farthest_point+1)

'''
#B - Sandwhich Number
'''
import sys
S = sys.stdin.readline().strip()
if len(S)!=8:
    print("No")
else:
    f_letter=S[0]
    l_letter=S[7]
    number=S[1:7]
    if f_letter.isupper() and l_letter.isupper():
        if number.isdigit() and int(number)>=100000 and int(number)<=999999:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
'''

#B - ABCDEFG
'''
import sys
p,q=sys.stdin.readline().split()
letters=["A","B","C","D","E","F","G"]
distances=[3,1,4,1,5,9]
index_p=0
index_q=0
for i,letter in enumerate(letters):
    if p==letter:
        index_p=i
    elif q==letter:
        index_q=i

max_index=max(index_p,index_q)
min_index=min(index_p,index_q)
to_be_added=list(distances[min_index:max_index])
sum=sum(to_be_added)
print(sum)
'''

#B - Piano
import sys
W,B=map(int,sys.stdin.readline().split())
S = "wbwbwwbwbwbw"
check_W=0
check_B=0
goal=str("w"*W)+str("b"*B)
for i in range(0,len(S)):
    substring=""
    equal=False
    for j in range(i,len(S)):
        substring+=S[j]
        if substring==goal:
            equal=True

    if equal:
        print("Yes")
        break

if not equal:
    print("No")



            


    

    
        

    









