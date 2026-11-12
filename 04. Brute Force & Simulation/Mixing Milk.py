import sys
Bucket_sizes=[]
Bucket_vol=[]
for i in range(3):
    size,vol=map(int,sys.stdin.readline().split())
    Bucket_sizes.append(size)
    Bucket_vol.append(vol)

operations = 0
while operations <100:
    for i,volume in enumerate(Bucket_vol):
        if operations>=100:
            break
        if i ==2:
            Bucket_vol[0]+=volume
            if Bucket_vol[0]> Bucket_sizes[0]:
                remaining=Bucket_vol[0]-Bucket_sizes[0]
                Bucket_vol[0]=Bucket_sizes[0]
                Bucket_vol[2]=remaining
            else:
                Bucket_vol[2]=0
        else:
            Bucket_vol[i+1]+=volume
            if Bucket_vol[i+1]>Bucket_sizes[i+1]:
                remaining= Bucket_vol[i+1]-Bucket_sizes[i+1]
                Bucket_vol[i+1]=Bucket_sizes[i+1]
                Bucket_vol[i]=remaining
            else:
                Bucket_vol[i]=0
        operations+=1

for volume in Bucket_vol:
    print(volume)
