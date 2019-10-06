s=input()
k=int(input())
ans=0
from itertools import*
g=[len(list(v))for k,v in groupby(s)]
for i in g:
    ans+=i//2
ans*=k
if s[0]==s[-1] and g[0]%2>0 and g[-1]%2>0:
    if len(s)==g[0]:
        ans+=k//2
    else:
        ans+=k-1
print(ans)
