n=int(input())

#素因数分解
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

import math

l=factorize(math.factorial(n))

a74=0
a24=0
a14=0
a4=0
a2=0

for i,j in l:
    if int(j)>=74:
        a74+=1
        a24+=1
        a14+=1
        a4+=1
        a2+=1
    elif int(j)>=24:
        a2+=1
        a24+=1
        a14+=1
        a4+=1
    elif int(j)>=14:
        a2+=1
        a4+=1
        a14+=1
    elif int(j)>=4:
        a2+=1
        a4+=1
    elif int(j)>=2:
        a2+=1


if a74+a24*(a2-1)+a14*(a4-1)+a4*a4*0.5*(a2-2)>=0:
    print(int(a74+a24*(a2-1)+a14*(a4-1)+a4*(a4-1)*0.5*(a2-2)))
else:
    print(0)
        
        
        
        
        
        
        
        
        