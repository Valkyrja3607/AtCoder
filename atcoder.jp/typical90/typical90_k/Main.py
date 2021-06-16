n=int(input())
l=[list(map(int,input().split()))for i in range(n)]
l.sort()
dp=[0]*5001
for d,c,s in l:
    for i in range(1,l[-1][0])[::-1]:
        if dp[i]!=0 and i+c<=d:
            dp[i+c]=max(dp[i]+s,dp[i+c])
    if c<=d:
        dp[c]=max(dp[c],s)
print(max(dp))