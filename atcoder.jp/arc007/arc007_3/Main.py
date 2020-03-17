s=input()
n=len(s)
l=[]
for i in s:
    if i=="o":
        l.append(True)
    else:
        l.append(False)
ll=[l]
for i in range(1,n):
    ll.append(l[i:]+l[:i])
import numpy as np
ll=np.array(ll)
ans=10**18
for i in range(1<<n):
    tmp=np.array([False]*n)
    t=0
    for j in range(n):
        if i>>j&1:
            t+=1
            tmp|=ll[j]
    if tmp.sum()==n:
        ans=min(ans,t)

print(ans)


    
    









