x,y=[int(j) for j in input().split()]
U = 2*10**6
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

if (2*y-x)//3==(2*y-x)/3 and (2*x-y)//3==(2*x-y)/3:
    i=(2*y-x)//3
    j=(2*x-y)//3
    print(comb(i+j,min(i,j)))
else:
    print(0)
