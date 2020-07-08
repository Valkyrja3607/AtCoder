n,c=map(int,input().split())
a=[int(j)for j in input().split()]
l=[[]for i in range(c+1)]
for i,j in enumerate(a,1):l[j].append(i)
U=2*10**5
mod=67280421310721
fact=[1]*(U+1)
fact_inv=[1]*(U+1)

for i in range(1,U+1):
    fact[i]=(fact[i-1]*i)%mod
fact_inv[U]=pow(fact[U],mod-2,mod)

for i in range(U,0,-1):
	fact_inv[i-1]=(fact_inv[i]*i)%mod
def comb(n,k):
    if k<0 or k>n:
        return 0
    x=fact[n]
    x*=fact_inv[k]
    x%=mod
    x*=fact_inv[n-k]
    x%=mod
    return x
ans=n+comb(n,2)
for i in range(1,c+1):
    tmp=0
    for p,q in zip([0]+l[i],l[i]+[n+1]):
        tmp+=comb(q-p-1,2)+q-p-1
    print(ans-tmp)