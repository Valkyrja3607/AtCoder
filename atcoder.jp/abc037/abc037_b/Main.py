n,q=[int(j) for j in input().split()]
import numpy as np
ll=np.zeros(n,dtype="int64")
for i in range(q):
    l,r,t=[int(j) for j in input().split()]
    ll[l-1:r]=t
for i in ll:
    print(i)
