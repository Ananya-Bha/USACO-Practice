#WEEK 1 PROBLEMS:

#A PILING UP:
'''
import sys
R = int(sys.stdin.readline())
if R>=1 and R<100:
    print(100-R)
elif R>=100 and R<200:
    print(200-R)
elif R>=200 and R<300:
    print(300-R)
elif R>=300 and R<400:
    print(400-R)
'''

#A WRONG ANSWER:
'''
import sys
import random
A,B= map(int,sys.stdin.readline().split())
numbers=[0,1,2,3,4,5,6,7,8,9]
sum=A+B
numbers.remove(sum)
print(numbers)
value=random.choice(numbers)
print(value)
'''

#A 369
'''
import sys
A,B= map(int,sys.stdin.readline().split())
values=set()
values.add(2*A-B)
values.add(2*B-A)
if (A+B)%2==0:
    values.add((A+B)//2)

print(len(values))
'''

#A WHO ATE THE CAKE?
'''
import sys
A, B= map(int,sys.stdin.readline().split())
people=[1,2,3]
people.remove(A)
if  B in people:
    people.remove(B)
if len(people)==1:
    print(people[0])
else:
    print(-1)
'''

#A EQUALLY
'''
import sys
A, B, C= map(int,sys.stdin.readline().split())
if (A+B == C) or (B+C==A) or (A+C==B) or (A==B==C):
    print("Yes")
else:
    print("No")
'''

#A RAISE BOTH HANDS
'''
import sys
L, R = map(int,sys.stdin.readline().split())
if (L==1 and R==1) or (L==0 and R==0):
    print("Invalid")
elif L==1 and R==0:
    print("Yes")
elif L==0 and R==1:
    print("No")
'''

#A 9x9
'''
import sys
A, B= map(int,sys.stdin.readline().split())
if (A<=9 and A>=1) and (B>=1 and B<=9):
    print(A*B)
else:
    print(-1)
'''

#A FOUR DIGITS
'''
import sys
s = sys.stdin.readline().strip()
s = str(s)
while len(s)<4:
    s = "0"+s
print(s)
'''

#A tcdr
'''
import sys
S = sys.stdin.readline().strip()
S=S.replace("a","")
S=S.replace("e","")
S=S.replace("i","")
S=S.replace("o","")
S=S.replace("u","")
print(S)
'''

#A NEW SCHEME
'''
import sys
S1, S2,S3,S4,S5,S6,S7,S8 = map(int,sys.stdin.readline().split())
numbers=[S1, S2,S3,S4,S5,S6,S7,S8]

if (numbers==sorted(numbers)):
    if numbers[0]%25==0 and numbers[1]%25==0:
        count=0
        for i in range(8):
            if numbers[i]<=675 and numbers[i]>=100:
                count+=1
        if count==8:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")
'''

#A THE BOTTOM OF THE NINTH
'''
import sys
Takahashi = list(map(int,sys.stdin.readline().split()))
Aoki = list(map(int,sys.stdin.readline().split()))
total_T = sum(Takahashi)
total_A = sum(Aoki)

if total_T>=total_A:
  difference=total_T-total_A
  print(difference+1)
'''

#B FIZZBUZZ SUM
'''
N=int(input())
sum=0
for number in range(1,N+1):
    if (number%3== 0 and number%5==0) or (number%3==0) or (number%5==0):
        continue
    else:
        sum+=number
print(sum)
'''

#B REMOVE IT
'''
import sys
N,X= map(int,sys.stdin.readline().split())
Sequence = list(map(int,sys.stdin.readline().split()))

answer=[]
for i in range(N):
    if Sequence[i]==X:
        continue
    else:
        answer.append(Sequence[i])

print(*answer)
'''

#B ATCODE CONDOMINIUM
'''
import sys
N, K = map(int,sys.stdin.readline().split())
sum=0
for i in range(1,N+1):
    for j in range(1,K+1):
        room_number=str(i)+str(0)+str(j)
        sum+=int(room_number)
        
print(sum)
'''

#B CAN YOU BUY ALL OF THEM?
'''
import sys
N,X=map(int,sys.stdin.readline().split())
product_prices=list(map(int,sys.stdin.readline().split()))
total_product_prices=0
for index,price in enumerate(product_prices):
    if index%2==1:
        total_product_prices+=price-1
    else:
        total_product_prices+=price

if total_product_prices>X:
    print("No")
else:
    print("Yes")
'''

#DENTIST AOKI
'''
import sys
N,Q=map(int,sys.stdin.readline().split())
teeth_to_fix=list(map(int,sys.stdin.readline().split()))
teeth_alr_fixed=set()
for tooth_no in teeth_to_fix:
    if tooth_no in teeth_alr_fixed:
        N+=1
        teeth_alr_fixed.remove(tooth_no)
    else:
        N-=1
        teeth_alr_fixed.add(tooth_no)

print(N)
'''

#B PREFIX & SUFFIX
'''
import sys
N, M=map(int,sys.stdin.readline().split())
S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()
prefix=False
suffix=False

sfirst=T[0:N]
slast=T[-N:]
if S == sfirst:
    prefix=True
if S== slast:
    suffix=True

if suffix and prefix:
    print(0)
elif suffix and not prefix:
    print(2)
elif not suffix and prefix:
    print(1)
else:
    print(3)
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

#B The middle Day
import sys
M = int(sys.stdin.readline())
Days = list(map(int,sys.stdin.readline().split()))

Total_days=sum(Days)
Middle_day=(Total_days+1)/2
sum_till_now=0
for month in range(M):
    for day in range(Days[month]):
        sum_till_now+=1
        if sum_till_now==Middle_day:
            print(f"{month+1} {day+1}")
            break
        
