n=int(input())
xy=[]
for i in range(n):
    a=[int(j) for j in input().split()]
    xy.append(a)

if n==1:
    print(1)
    import sys
    sys.exit()
l=[]
ans=0
import itertools
for a,b in itertools.combinations(xy,2):
    p=(a[0]-b[0])
    q=(a[1]-b[1])
    if p!=0 or q!=0:
        l.append((p,q))
        l.append((-p,-q))

import collections
c=collections.Counter(l)
p=c.most_common()

for i in p:
   ans=max(ans,i[1])
print(n-ans)