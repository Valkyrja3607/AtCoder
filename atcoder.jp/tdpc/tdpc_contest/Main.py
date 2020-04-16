n=int(input())
a=[int(j) for j in input().split()]
dp=[0]*(100*n+1)
dp[0]=1
for i in a:
    for j in range(100*n+1)[::-1]:
        if dp[j]!=0:
            dp[i+j]=1

print(sum(dp))