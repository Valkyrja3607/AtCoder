n,q=[int(j) for j in input().split()]
a=[int(j) for j in input().split()]
c=[1]+[int(j) for j in input().split()]+[1]
mod=10**9+7
l=[pow(i,j,mod)for i,j in zip(a,a[1:])]
from itertools import accumulate
l=[0]+list(accumulate(l))
ans=0
for i,j in zip(c,c[1:]):
    ans+=abs(l[j-1]-l[i-1])
    ans%=mod
print(ans)