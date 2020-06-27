n,a=map(int,input().split())
x=[int(j)-a for j in input().split()]
from collections import defaultdict
dp=[defaultdict(int)for i in range(n+1)]
dp[0][0]=1
for i,j in enumerate(x,1):
    l=dp[i-1].copy()
    for k in dp[i-1]:
        l[k+j]+=dp[i-1][k]
    dp[i]=l

print(dp[-1][0]-1)