n=int(input())
a=sorted(list(map(int,input().split())))[::-1]
mod=10**9+7
ans=0
for i in range(n):
    p=pow(4,n-1,mod)*(i+2)%mod
    ans=(ans+p*a[i])%mod
print(ans)