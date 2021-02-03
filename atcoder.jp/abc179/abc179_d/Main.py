n,k=map(int,input().split())
lr=[[int(j)for j in input().split()]for i in range(k)]
mod=998244353
dp=[0]*(n*2+1)
dp[0]=1
sdp=[1]*(n*2+1)
for i in range(n):
    for j in range(k):
        l,r=lr[j]
        dp[i]=(dp[i]+sdp[i-l]-sdp[i-r-1])%mod
    sdp[i]=(sdp[i-1]+dp[i])%mod
print(dp[n-1])