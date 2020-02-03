from subprocess import*
call(('pypy3','-c',"""
h,n=[int(j) for j in input().split()]
ab=[[int(j) for j in input().split()] for i in range(n)]
dp=[10**18]*(h+1)
dp[0]=0
ans=10**18
for a,b in ab:
    for i in range(h+1):
        if dp[i]!=10**18:
            if i+a<h:
                if dp[i]+b<dp[i+a]:
                    dp[i+a]=dp[i]+b
            else:
                if dp[i]+b<ans:
                    ans=dp[i]+b
 
print(ans)

"""))