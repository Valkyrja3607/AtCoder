n,m=map(int,input().split())
l=[[] for i in range(n)]
for i in range(m):
    p=[int(j) for j in input().split()]
    l[p[1]-1].append(p[0]-1)

dp=[-1]*n
import sys
sys.setrecursionlimit(10**6)
def f(v):
    if dp[v]!=-1:
        return dp[v]
    p=0
    for i in l[v]:
        p=max(p,f(i)+1)
    dp[v]=p
    return dp[v]

for i in range(n):
    f(i)

print(max(dp))