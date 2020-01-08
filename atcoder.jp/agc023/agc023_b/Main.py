import numpy as np
n=int(input())
s=np.array([list(input()) for i in range(n)])
s=np.concatenate([s,s])
ans=0
for i in range(n):
    l=s[i:i+n]
    if (l==l.T).all():
        ans+=n
print(ans)