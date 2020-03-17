n=int(input())
l=[int(j) for j in input().split()]
ans=l[-1]
l=l[:-1]
dp=[[0]*21 for i in range(n-1)]
dp[0][l[0]]=1
for i in range(1,n-1):
    for j in range(21):
        if dp[i-1][j]>0:
            if j+l[i]<=20:
                dp[i][j+l[i]]+=dp[i-1][j]
            if j-l[i]>=0:
                dp[i][j-l[i]]+=dp[i-1][j]

print(dp[-1][ans])

