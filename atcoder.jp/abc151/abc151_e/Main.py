n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
U = 2*10**5
MOD = 10**9+7
fact = [1]*(U+1)
fact_inv = [1]*(U+1)
for i in range(1,U+1):
  fact[i] = (fact[i-1]*i)%MOD
fact_inv[U] = pow(fact[U],MOD-2,MOD)
for i in range(U,0,-1):
	fact_inv[i-1] = (fact_inv[i]*i)%MOD
def comb(n,k):
  if k < 0 or k > n:
    return 0
  x = fact[n]
  x *= fact_inv[k]
  x %= MOD
  x *= fact_inv[n-k]
  x %= MOD
  return x

mod=10**9+7
p=a[:n-k+1][::-1]
q=a[k-1:]
ans=0
for i in range(1,len(p)+1):
    ans+=(q[i-1]-p[i-1])*comb(k-2+i,k-1)
    ans%=mod
print(ans)