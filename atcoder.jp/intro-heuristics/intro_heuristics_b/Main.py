import numpy as np
d=int(input())
c=[0]+[int(j)for j in input().split()]
s=[[0]+[int(j)for j in input().split()]for i in range(d)]
t=[int(input())for i in range(d)]
l=[0]*27
ans=0
for i,j in enumerate(t,1):
    ans+=s[i-1][j]
    l[j]=i
    for k in range(1,27):
        ans-=(i-l[k])*c[k]
    print(ans)