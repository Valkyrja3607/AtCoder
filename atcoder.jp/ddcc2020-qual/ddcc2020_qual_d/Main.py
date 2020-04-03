m=int(input())
dc=[[int(j) for j in input().split()] for i in range(m)]
s=0
k=0
for d,c in dc:
    s+=d*c
    k+=c
print((k-1)+(s-1)//9)