n=int(input())

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

def d(n):
    l=factorize(n)
    r=1
    for i,j in l:
        r*=int(j)+1
    return r
ans=0

import math
ans=d(math.factorial(n))%1000000007

print(ans)