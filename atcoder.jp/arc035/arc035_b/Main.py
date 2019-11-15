n=int(input())
t=[int(input()) for i in range(n)]
t.sort()
from itertools import*
g=[len(list(v))for k,v in groupby(t)]
tmp=0
ans=0
for i in t:
    tmp+=i
    ans+=tmp
print(ans)
ans=1
import math
mod=10**9+7
for i in g:
    ans*=math.factorial(i)
    ans=ans%mod
print(ans)