n=int(input())
a=[int(i) for i in input().split()]

l=[0]
def ruiseki(a):
    for i in range(len(a)):
        l.append(l[i]+a[i])

ruiseki(a)

import collections
cl=collections.Counter(l)


def c(n,m):
    import math
    if n-m<0:
        return 0
    return(math.factorial(n)//math.factorial(n-m)//math.factorial(m))
ans=0
for i in set(l):
    ans+=c(int(cl[i]),2)

print(ans)