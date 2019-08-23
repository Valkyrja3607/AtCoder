n,a=[int(i) for i in input().split()]
x=[int(i) for i in input().split()]
y=[i-a for i in x]
m=sum(x)+1
dp=[[0 for j in range(m*2+1)] for i in range(n+1)]
dp[0][0]=1
for i in range(1,n+1):
    for j in range(-m,1+m):
        if j-y[i-1]>=-m and j-y[i-1]<=1+m:
            dp[i][j]=dp[i-1][j]+dp[i-1][j-y[i-1]]
        else:
            dp[i][j]=dp[i-1][j]

print(dp[n][0]-1)
