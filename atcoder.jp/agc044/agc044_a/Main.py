t=int(input())
from functools import lru_cache
for _ in range(t):
    n,a,b,c,d=map(int,input().split())
    @lru_cache(maxsize=100000)
    def f(n):
        if n==0:
            return 0
        if n==1:
            return d
        ans=d*n
        q,r=divmod(n,2)
        if r==0:
            ans=min(ans,f(q)+a+d*r)
        else:
            ans=min(ans,f(q)+a+d*r,f(q+1)+a+d*(2-r))
        q,r=divmod(n,3)
        if r==0:
            ans=min(ans,f(q)+b+d*r)
        else:
            ans=min(ans,f(q)+b+d*r,f(q+1)+b+d*(3-r))
        q,r=divmod(n,5)
        if r==0:
            ans=min(ans,f(q)+c+d*r)
        else:
            ans=min(ans,f(q)+c+d*r,f(q+1)+c+d*(5-r))
        return ans
    print(f(n))