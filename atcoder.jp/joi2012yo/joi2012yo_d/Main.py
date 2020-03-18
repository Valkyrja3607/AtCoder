n,k=map(int,input().split())
dp=[[[0,0] for j in range(3)]for i in range(n)]
mod=10000
t=[[int(j) for j in input().split()] for i in range(k)]
d={i-1:v-1 for i,v in t}
for i in range(n):
    if i==0:
        if i in d:
            dp[0][d[i]][0]=1
        else:
            for j in range(3):
                dp[0][j][0]=1
    else:
        if i in d:
            j=d[i]
            dp[i][j][0]=sum(sum(dp[i-1][k])for k in range(3)if k!=j)%mod
            dp[i][j][1]=dp[i-1][j][0]
        else:
            for j in range(3):
                dp[i][j][0]=sum(sum(dp[i-1][k])for k in range(3)if k!=j)%mod
                dp[i][j][1]=dp[i-1][j][0]

print(sum(dp[-1][i][j]for i in range(3) for j in range(2))%mod)