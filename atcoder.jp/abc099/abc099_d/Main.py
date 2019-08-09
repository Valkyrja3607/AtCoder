n,C=map(int,input().split())
d=[]
c=[]
for i in range(C):
    d.append([int(j) for j in input().split()])
for i in range(n):
    c.append([int(j) for j in input().split()])
l1=[0 for i in range(C+1)]
l2=[0 for i in range(C+1)]
l3=[0 for i in range(C+1)]

for i in range(n):
    for j in  range(n):
        if (i+j+2)%3==0:
            for k in range(1,C+1):
                l1[k]+=d[c[i][j]-1][k-1]
        if (i+j+2)%3==1:
            for k in range(1,C+1):
                l2[k]+=d[c[i][j]-1][k-1]
        if (i+j+2)%3==2:
            for k in range(1,C+1):
                l3[k]+=d[c[i][j]-1][k-1]
ans=10**100
for i in range(1,C+1):
    for j in range(1,C+1):
        for k in range(1,C+1):
            if i!=j and i!=k and j!=k:
                ans=min(ans,l1[i]+l2[j]+l3[k])
print(ans)