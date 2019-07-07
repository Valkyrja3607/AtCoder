n,d=map(int,input().split())
x=[]
for i in range(n):
    p=[int(j) for j in input().split()]
    x.append(p)

ans=0
import itertools
for i,j in itertools.combinations(range(n),2):
    res=0
    for k in range(d):
        res+=(x[i][k]-x[j][k])**2
    q=res**0.5
    if q==q*10//10:
        ans+=1
print(ans)


