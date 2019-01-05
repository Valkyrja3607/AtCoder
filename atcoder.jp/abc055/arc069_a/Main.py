n,m=map(int,input().split())

ans=0
if 2*n<=m:
    ans+=n
    n=0
    m-=2*ans
elif 1<=n and 2<=m:
    ans+=m//2
    n-=m
    m-=(m//2)*2
   

ans+=m//4

print(ans)
