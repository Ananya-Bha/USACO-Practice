import sys
N = int(sys.stdin.readline())
prices = list(map(int, sys.stdin.readline().split()))

yen1 = 0
yen10 = 0
yen100 = 0

for price in prices:
    bills = (price + 999) // 1000
    change = bills * 1000 - price

    yen100 += change // 100
    yen10  += (change // 10) % 10
    yen1   += change % 10

print(yen1, yen10, yen100)
