import sys
input=sys.stdin.readline
import numpy as np
n=int(input())
a=np.array([int(j) for j in input().split()],dtype=np.int64)
ans=0
mod=10**9+7
for i in range(61):
    b=(a>>i)&1
    c=np.count_nonzero(b)
    ans+=(2**i)*c*(n-c)
    ans%=mod
print(ans)