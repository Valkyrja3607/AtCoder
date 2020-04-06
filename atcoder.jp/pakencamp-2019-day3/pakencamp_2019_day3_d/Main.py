import numpy as np
n=int(input())
s=np.array([list(input()) for i in range(5)])
from collections import Counter
l=[]
for i in range(n):
    l.append(Counter(s[:,i]))
dp=[[0]*3 for i in range(n)]
#W0 B1 R2
for i in range(n):
    if i==0:
        dp[0][0]=5-l[0]["W"]
        dp[0][1]=5-l[0]["B"]
        dp[0][2]=5-l[0]["R"]
        continue
    dp[i][0]=5-l[i]["W"]+min(dp[i-1][1],dp[i-1][2])
    dp[i][1]=5-l[i]["B"]+min(dp[i-1][0],dp[i-1][2])
    dp[i][2]=5-l[i]["R"]+min(dp[i-1][1],dp[i-1][0])

print(min(dp[-1]))