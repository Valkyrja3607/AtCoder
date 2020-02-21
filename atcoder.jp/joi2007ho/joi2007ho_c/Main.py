n=int(input())
l=[tuple(int(j) for j in input().split()) for i in range(n)]
ss=set(l)
ans=0

import itertools
for p,q in itertools.combinations(l,2):
    a,b=p
    c,d=q
    e=a-c
    f=b-d
    r,s=(a-f,b+e),(c-f,d+e)
    t,u=(a+f,b-e),(c+f,d-e)
    if (r in ss and s in ss) or (t in ss and u in ss):
        if e**2+f**2>ans:
            ans=e**2+f**2
print(ans)

