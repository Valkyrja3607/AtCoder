n=int(input())
ab=[]
l=[]
for i in range(n):
    a,b=[int(j) for j in input().split()]
    ab.append((a,b))
    l.append(a)
    l.append(b)
ans=10**20

import itertools
for x,y in itertools.combinations(l,2):
    tmp=0
    for a,b in ab:
        p,q=abs(a-x),abs(b-x)
        r,s=abs(a-y),abs(b-y)
        tmp+=abs(a-b)+min(p+s,q+r)
    ans=min(ans,tmp)
    
print(ans)



