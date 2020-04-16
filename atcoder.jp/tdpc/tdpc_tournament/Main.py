k=int(input())
r=[int(input())for i in range(1<<k)]
dp=[[0]*(k+1) for i in range(1<<k)]
for i in range(1<<k):
    dp[i][0]=1
import itertools
for i in range(1,k+1):
    for j in range(0,1<<k,1<<i):
        for p in range(j,j+(1<<(i-1))):
            for q in range(j+(1<<(i-1)),j+(1<<(i-1))+(1<<(i-1))):
                dp[p][i]+=1/(1+10**((r[q]-r[p])/400))*dp[p][i-1]*dp[q][i-1]
                dp[q][i]+=1/(1+10**((r[p]-r[q])/400))*dp[p][i-1]*dp[q][i-1]

for i in range(1<<k):
    print(dp[i][-1])