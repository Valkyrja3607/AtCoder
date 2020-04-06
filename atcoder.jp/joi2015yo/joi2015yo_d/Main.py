n,m=map(int,input().split())
d=[int(input())for i in range(n)]
c=[int(input())for i in range(m)]
dp=[[0]*m for i in range(n)]
dp[0][0]=c[0]*d[0]
for i in range(n):
    tmp=10**18
    for j in range(1,m):
        if i>j:
            continue
        if i==0:
            dp[i][j]=c[j]*d[0]
        else:
            tmp=min(tmp,dp[i-1][j-1])
            dp[i][j]=tmp+c[j]*d[i]
import numpy
ans=numpy.array(dp[-1])
print(ans[ans>0].min())