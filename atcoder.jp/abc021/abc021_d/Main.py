def comb(n,m):
    mod=10**9+7
    x,y=1,1
    for i in range(n-m+1,n+1):
        x*=i
        x%=mod
    for i in range(1,m+1):
        y*=i
        y%=mod
    if n-m<0:
        return 0
    return((x*pow(y,mod-2,mod))%mod)

n=int(input())
k=int(input())
print(comb(n+k-1,k))