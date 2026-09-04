"""
Farmer John has gone out for a walk down the road and thinks he may now be lost!

Along the road there are N farms (1≤N≤100) in a row. Farms unfortunately do not have house numbers, making it hard for Farmer John to figure out his location along the road. However, each farm does have a colorful mailbox along the side of the road, so Farmer John hopes that if he looks at the colors of the mailboxes nearest to him, he can uniquely determine where he is.

Each mailbox color is specified by a letter in the range A..Z, so the sequence of N mailboxes down the road can be represented by a string of length N containing letters in the range A..Z. Some mailboxes may have the same colors as other mailboxes. Farmer John wants to know what is the smallest value of K such that if he looks at any sequence of K consecutive mailboxes, he can uniquely determine the location of that sequence along the road.

For example, suppose the sequence of mailboxes along the road is 'ABCDABC'. Farmer John cannot set K=3, since if he sees 'ABC', there are two possible locations along the road where this consecutive set of colors might be. The smallest value of K that works is K=4, since if he looks at any consecutive set of 4 mailboxes, this sequence of colors uniquely determines his position along the road.

INPUT FORMAT (file whereami.in):
The first line of input contains N, and the second line contains a string of N characters, each in the range A..Z.

OUTPUT FORMAT (file whereami.out):
Print a line containing a single integer, specifying the smallest value of K that solves Farmer John's problem.

SAMPLE INPUT:

7
ABCDABC    

SAMPLE OUTPUT:

4
"""

#k = 0 "ABCDABC"
#k = 1 "AB", "BC", "CD", "DA", "AB", "BC"

import sys
sys.stdin = open("whereami.in","r")
sys.stdout = open("whereami.out", "w")
mailboxes = sys.stdin.read().strip().splitlines()
N = int(mailboxes[0])
s = mailboxes[1]

for k in range(N):
    seen = set()
    for i in range(N-k):
        seen.add(s[i:i+k])
    if len(seen)==(N-k):
        print(k+1)
        


#Are we at a unique place at 1 element? No
#Are we at a unique place at 2 elements? No
#Are we at a unique place at 3 elements? No
#Are we at a unique place at 4 elements? Yes

#O(1)? No
#O(N)? No
#O(N^2)? No
#O(N^3)? Yes
