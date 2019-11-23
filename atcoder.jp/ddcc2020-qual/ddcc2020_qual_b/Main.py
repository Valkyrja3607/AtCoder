n=int(input())
a=[int(j) for j in input().split()]
from itertools import accumulate
l=[0]+list(accumulate(a))
ans=10**18
for i in range(n+1):
    ans=min(ans,abs(l[i]-(l[-1]-l[i])))
print(ans)
