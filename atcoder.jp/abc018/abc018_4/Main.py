n,m,p,q,r=map(int,input().split())
xyz=[]
l=[[] for i in range(n+1)]
for i in range(r):
    tmp=[int(j) for j in input().split()]
    xyz.append(tmp)
    l[tmp[0]].append([tmp[1],tmp[2]])

import itertools
from operator import itemgetter
ans=0
for x in itertools.combinations(range(1,n+1),p):
    ll=[0 for i in range(m+1)]
    t=0
    for i in x:
        for j,k in l[i]:
            ll[j]+=k
    ll.sort()
    ll.reverse()
    t=sum(ll[0:q])
    ans=max(ans,t)
print(ans)