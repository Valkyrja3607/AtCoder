n,m,k=map(int,input().split())
a=[int(j)for j in input().split()]
b=[int(j)for j in input().split()]
from itertools import accumulate
a=[0]+list(accumulate(a))
b=[0]+list(accumulate(b))
ans=0
j=m
for i in range(n+1):
    if a[i]<=k:
        while a[i]+b[j]>k:j-=1
        ans=max(ans,i+j)
print(ans)