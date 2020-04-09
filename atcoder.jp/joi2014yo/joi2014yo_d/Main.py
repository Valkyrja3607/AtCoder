n=int(input())
s=input()
mod=10**4+7
dp=[[0]*8 for i in range(n)]

for i,c in enumerate(s):
    if i==0:
        if c=="J":
            for j in [1,3,5,7]:
                dp[i][j]=1
        if c=="O":
            for j in [3,7]:
                dp[i][j]=1
        else:
            for j in [5,7]:
                dp[i][j]=1
    else:
        if c=="J":
            for j in [1,3,5,7]:
                for k in range(8):
                    if j&k:
                        dp[i][j]+=dp[i-1][k]
                        dp[i][j]%=mod
        elif c=="O":
            for j in [2,3,6,7]:
                for k in range(8):
                    if j&k:
                        dp[i][j]+=dp[i-1][k]
                        dp[i][j]%=mod
        else:
            for j in [4,5,6,7]:
                for k in range(8):
                    if j&k:
                        dp[i][j]+=dp[i-1][k]
                        dp[i][j]%=mod
print(sum(dp[-1])%mod)