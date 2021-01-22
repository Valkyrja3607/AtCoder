n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
dp=[[0]*(m+1) for i in range(n+1)]
for i in range(n+1):
    dp[i][0]=i
for i in range(m+1):
    dp[0][i]=i
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j]=min(dp[i][j-1]+1,dp[i-1][j]+1,dp[i-1][j-1]+(a[i-1]!=b[j-1]))
print(dp[-1][-1])