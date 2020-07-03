n=int(input())
a=[int(j)for j in input().split()]
import collections
l=collections.Counter()
m=0
ans=0
for i,j in enumerate(a,1):
    if l[j]<m:
        t=i-m
    else:
        t=i-l[j]
        m=l[j]
    l[j]=i
    ans=max(ans,t)
print(ans)