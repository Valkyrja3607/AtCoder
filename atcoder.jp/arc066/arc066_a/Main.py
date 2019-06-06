n=int(input())
a=[int(i) for i in input().split()]

import collections
c=collections.Counter(a)
l=len(c)
ans=1

for i in range((n-1)%2,n,2):
    if i==0:
        if c[0]!=1:
            ans=0
    elif c[i]==2:
        ans*=2
    else:
        ans=0
    ans=ans%(10**9+7)


print(ans)


