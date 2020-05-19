import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n=int(input())
mod=10**9+7
l=[[]for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    l[a].append(b)
    l[b].append(a)
def dp(x,par):
    res_w,res_t=1,1
    for y in l[x]:
        if y==par:
            continue
        w,t=dp(y,x)
        res_w=(res_w*w)%mod
        res_t=(res_t*t)%mod
    w,t=res_t,(res_t+res_w)%mod
    return w,t
print(dp(1,0)[1])