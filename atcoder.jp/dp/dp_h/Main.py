h,w=map(int,input().split())
a=[]
mod=10**9+7
h+=2
w+=2
a.append("#"*w)
for i in range(h-2):
    a.append("#"+input()+"#")
a.append("#"*w)

dp=[[0 for i in range(w)]for j in range(h)]
dp[0][1]=1
for i in range(1,h-1):
    for j in range(1,w-1):
        if a[i][j]==".":
            dp[i][j]=(dp[i-1][j]+dp[i][j-1])%mod

print(dp[h-2][w-2])