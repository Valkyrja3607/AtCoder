n,q=[int(j) for j in input().split()]
l=[0]*20001
ll=[[int(j) for j in input().split()]for i in range(n)]
tmp=0
from math import *
for x,r,h in ll:
    for i in range(x,x+h)[::-1]:
        l[i]+=((x+h-i)*pi*(r*(x+h-i)/h)**2)/3-((x+h-i-1)*pi*(r*(x+h-i-1)/h)**2)/3
for i in range(20000)[::-1]:
    l[i]+=l[i+1]
for i in range(q):
    a,b=[int(j) for j in input().split()]
    print(l[a]-l[b])