import sys
input = sys.stdin.readline
n,k=[int(j) for j in input().split()]
a=[int(j) for j in input().split()]
mod=10**9+7
import numpy as np
dp=np.zeros((n+1,k+1),dtype=np.int64)
dp[0][0]=1
for i in range(n):
    dp[i+1]=dp[i]
    dp[i+1,a[i]+1:]-=dp[i,:-(a[i]+1)]
    np.cumsum(dp[i+1],out=dp[i+1])
    dp[i+1]%=mod
print(dp[n][k])