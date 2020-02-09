n,k=[int(j) for j in input().split()]
p=[int(j) for j in input().split()]
from itertools import accumulate
l=[0]+list(accumulate(p))
t=0
a,b=0,0
for i in range(n-k+1):
    if t<l[i+k]-l[i]:
        t=l[i+k]-l[i]
        a,b=i+k,i
ans=0
for i in range(b,a):
    j=p[i]
    ans+=j*(j+1)//2/j
    
print(ans)