n,m=map(int,input().split())
a=([int(j) for j in input().split()]+[0])[::-1]
b=([int(j) for j in input().split()]+[0])[::-1]

dp=[[0]*(m+1) for i in range(n+1)]

for i in range(n+1):
    for j in range(m+1):
        if (i+j)%2==(n+m)%2:
            dp[i][j]=max(dp[i-1][j]+a[i],dp[i][j-1]+b[j])
        else:
            if i==0:
                dp[i][j]=dp[i][j-1]
            elif j==0:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])
print(dp[-1][-1])