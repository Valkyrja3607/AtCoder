n,d=map(int,input().split())
from fractions import gcd
from collections import Counter
dp=[Counter()for i in range(n+1)]
dp[0][d]=1
for i in range(n):
    for j in dp[i]:
        for k in range(1,7):
            dp[i+1][j//gcd(j,k)]+=dp[i][j]/6
print(dp[n][1])