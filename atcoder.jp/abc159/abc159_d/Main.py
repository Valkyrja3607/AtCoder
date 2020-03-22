n=int(input())
a=[int(j) for j in input().split()]
from collections import Counter
c=Counter()
for i in a:
    c[i]+=1
ans=0
for i in c:
    ans+=c[i]*(c[i]-1)//2
for i in a:
    print(ans-c[i]*(c[i]-1)//2+(c[i]-1)*(c[i]-2)//2)