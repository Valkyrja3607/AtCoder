n=int(input())
mod=10**9+7
ans=1
for i in range(1,1+n):
    ans*=i
    ans=ans%mod
print(ans)