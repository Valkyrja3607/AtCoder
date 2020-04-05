import numpy as np
n,k=[int(j) for j in input().split()]
a=np.array([int(j) for j in input().split()])
aa=a.cumsum()
l=aa[:,None]-aa[None,:]+a[None,:]
l=l.flatten()
l=l[l>0]

def f(x):
    return np.sum(l&x==x)>=k

left=0
right=1<<40
while right-left>1:
    mid=(left+right)//2
    if f(mid):
        left=mid
    else:
        right=mid
print(left)