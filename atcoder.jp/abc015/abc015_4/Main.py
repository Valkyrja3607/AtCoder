w=int(input())
n,k=map(int,input().split())
import numpy as np
dp=np.array([[0]*(k+1) for i in range(w+1)])
for i in range(n):
    a,b=map(int,input().split())
    dp[a:,1:]=np.maximum(dp[:-a,:-1]+b,dp[a:,1:])

print(dp.max())
