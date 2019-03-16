n=int(input())
s=input()
l=list(s)
sl=set(l)

import collections

c=collections.Counter(l)
ans=1
for i in sl:
    ans*=(c[i]+1)

print((ans-1)%1000000007)