n,m=map(int,input().split())
import numpy as np
a=np.array([[int(j) for j in input().split()]for _ in range(n)])
tmp=0
import itertools
for i,j in itertools.combinations(range(m),2):
    tmp=max(tmp,np.maximum(a[:,i],a[:,j]).sum())

print(tmp)


