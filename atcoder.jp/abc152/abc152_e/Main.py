n=int(input())
a=[int(j) for j in input().split()]
t=1
mod=10**9+7
from fractions import*
for i in a:
    t*=i//gcd(t,i)
print(sum(t//i for i in a)%mod)