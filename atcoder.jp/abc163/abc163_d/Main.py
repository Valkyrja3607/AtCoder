n,k=map(int,input().split())
mod=10**9+7
ans=0
for i in range(k,n+2):
    ans=(ans+(n-i+1)*i+1)%mod
print(ans)