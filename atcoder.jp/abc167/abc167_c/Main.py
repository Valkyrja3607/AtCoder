n,m,x=[int(j) for j in input().split()]
l=[]
import numpy as np
for i in range(n):
    tmp=[int(j) for j in input().split()]
    l.append((tmp[0],np.array(tmp[1:])))
ans=10**18
import itertools
for i in itertools.product(range(2),repeat=n):
    tl=np.array([0]*m)
    tc=0
    for idx,j in enumerate(i):
        if j==1:
            c,ll=l[idx]
            tc+=c
            tl+=ll
    if len(tl[tl>=x])==m:
        ans=min(ans,tc)

if ans!=10**18:
    print(ans)
else:
    print(-1)