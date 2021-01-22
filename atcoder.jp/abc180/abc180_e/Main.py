n=int(input())
l=[[int(j)for j in input().split()]for i in range(n)]
dp=[[10**18]*n for i in range(1<<n)]
dp[0][0]=0
for i in range(1<<n):
    for j in range(n):
        for k in range(n):
            res=abs(l[j][0]-l[k][0])+abs(l[j][1]-l[k][1])+max(0,l[k][2]-l[j][2])
            dp[i|1<<k][k]=min(dp[i|1<<k][k],dp[i][j]+res)
print(dp[-1][0])