n,k=map(int,input().split())
mod=10**9+7
dp=[[0,0]for i in range(n+1)]
dp[0]=[1,1]
dp[1][0]=1
for i in range(2,n+1):
    dp[i][1]=sum(dp[i-1])%mod
    dp[i][0]=sum(dp[i-1])%mod
    if i>=k:
        dp[i][0]=(dp[i][0]-dp[i-k][1])%mod
print(dp[n][0])