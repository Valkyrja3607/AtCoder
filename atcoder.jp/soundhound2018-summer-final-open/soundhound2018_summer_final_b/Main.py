n,k=map(int,input().split())
b=[]
for i in range(n):
    b.append(int(input()))

dp=[0]*n
m=0
for i in range(n):
    if i<k-1:
        dp[i]=dp[i-1]+b[i]
    else:
        m=max(m,dp[i-k])
        dp[i]=max(m,dp[i-1]+b[i])
print(dp[-1])

    