s=input()
n=len(s)
from collections import Counter
l=Counter()
for i in "abcdefghijklmnopqrstuvwxyz":
    l[i]=[]
for i in range(n):
    l[s[i]].append(i)
t=input()
m=len(t)
ans=0
p=-1
import bisect
for i in range(m):
    c=t[i]
    ll=l[c]
    if ll==[]:
        print(-1)
        exit()
    if ll[-1]<=p:
        ans+=n
        p=ll[0]
        if i==m-1:
            ans+=p+1
    else:
        p=ll[bisect.bisect_right(ll,p)]
        if i==m-1:
            ans+=p+1
print(ans)
