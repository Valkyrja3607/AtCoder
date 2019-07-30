s=input()
n=len(s)
mod=10**9+7
dp=[[0 for i in range(13)] for j in range(n+1)]
if s[-1]=="?":
    for i in range(10):
        dp[1][i]=1
else:
    p=int(s[-1])
    dp[1][p]=1
for i in range(1,1+n):
    if s[-i]=="?":
        for j in range(10):
            p=j*pow(10,i-1,13)%13
            for k in range(13):
                dp[i][k+p-13]+=dp[i-1][k]
                dp[i][k+p-13]=dp[i][k+p-13]%mod
    else:
        p=int(s[-i])*pow(10,i-1,13)%13
        for k in range(13):
            dp[i][k+p-13]+=dp[i-1][k]
            dp[i][k+p-13]=dp[i][k+p-13]%mod
print(dp[-1][5])