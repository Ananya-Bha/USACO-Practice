import sys
N, M = map(int, sys.stdin.readline().split())
spotted_genomes=[]
unspotted_genomes=[]
for i in range(N):
    to_add=sys.stdin.readline().strip()
    spotted_genomes.append(to_add)
for i in range(N):
    to_add=sys.stdin.readline().strip()
    unspotted_genomes.append(to_add)

print(N,M)
print(spotted_genomes)
print(unspotted_genomes)         

locations=0

for pos in range(M):
    spotted_letters=[]
    unspotted_letters=[]
    for genome in range(N):
        spotted_letters.append(spotted_genomes[genome][pos])
        unspotted_letters.append(unspotted_genomes[genome][pos])
    valid = True
    for letter in spotted_letters:  
        if letter in unspotted_letters:
            valid = False
            break
    if valid:
        locations+=1

print(locations)
