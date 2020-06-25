n,m=map(int,input().split())
mod=10**9+7
def factorize(n):
    fct=[]
    b,e=2,0
    while b*b<=n:
        while n%b==0:
            n=n//b
            e=e+1
        if e>0:
            fct.append((b,e))
        b,e=b+1,0
    if n>1:
        fct.append((n,1))
    return fct

U=2*10**5
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
import math
l=factorize(abs(n))
c=0
d=1
ans=1
for i,j in l:
    ans=(ans*comb(j+m-1,j))%mod
p=0
if n>0:
    for i in range(0,m+1,2):
        p=(p+comb(m,i))%mod
else:
    for i in range(1,m+1,2):
        p=(p+comb(m,i))%mod
print(ans*p%mod)