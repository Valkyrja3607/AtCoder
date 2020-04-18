from subprocess import*
call(('pypy3','-c',"""
d=int(input())
n=int(input())
m=len(str(n))
mod=10**9+7
K=list(map(int,list(str(n))))
dp=[[[0,0]for j in range(d)]for i in range(m+1)]
dp[0][0][0]=1
for i in range(1,m+1):
    for j in range(d):
        for k in range(10):
            if k==K[i-1]:
                dp[i][(j+k)%d][0]=(dp[i][(j+k)%d][0]+dp[i-1][j][0])%mod
            elif k<K[i-1]:
                dp[i][(j+k)%d][1]+=dp[i-1][j][0]
            dp[i][(j+k)%d][1]=(dp[i][(j+k)%d][1]+dp[i-1][j][1])%mod
print(sum(dp[-1][0])%mod-1)
"""))