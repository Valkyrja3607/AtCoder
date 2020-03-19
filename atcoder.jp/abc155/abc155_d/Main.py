n,k=[int(j) for j in input().split()]
from numpy import *
a=array([int(j) for j in input().split()])
a.sort()
lm=a[a<0]
lp=a[a>0]
lz=a[a==0]
np=len(lp)
nm=len(lm)
nz=len(lz)

import bisect
import math
def f(x):
    c=0
    if x>=0:
        c+=nz*n
    c+=searchsorted(a,x//lp,side="right").sum()
    c+=(n-searchsorted(a,(-x-1)//(-lm),side="right")).sum()
    c-=count_nonzero(a*a<=x)
    return c//2

left=-10**20
right=10**20
while right-left>1:
    mid=(left+right)//2
    if f(mid)>=k:
        right=mid
    else:
        left=mid
print(right)



