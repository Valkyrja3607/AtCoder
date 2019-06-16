n,k=map(int,input().split())
a=[int(j) for j in input().split()]

from itertools import accumulate
l=[0]+list(accumulate(a))
ans=0

import bisect
for i in range(n+1):
    m=bisect.bisect_left(l,l[i]+k)
    ans+=n+1-m

print(ans)

