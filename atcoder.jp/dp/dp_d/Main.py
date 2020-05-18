n,W=[int(j) for j in input().split()]
wv=[[int(j) for j in input().split()]for i in range(n)]
import numpy as np
dp=np.zeros(W+1,dtype=np.int64)
for w,v in wv:
    dp[w:]=np.maximum(dp[w:],dp[:-w]+v)
print(dp.max())