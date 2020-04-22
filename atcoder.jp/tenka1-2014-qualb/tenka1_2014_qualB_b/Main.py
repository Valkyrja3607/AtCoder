n=int(input())
s=input()
m=len(s)
l=[input()for i in range(n)]
ll=[len(t)for t in l]
dp=[0]*(m+1)
dp[0]=1
mod=10**9+7
for i in range(m):
    for t,j in zip(l,ll):
        if i+j<=m:
            if t==s[i:i+j]:
                dp[i+j]=(dp[i+j]+dp[i])%mod
print(dp[-1])