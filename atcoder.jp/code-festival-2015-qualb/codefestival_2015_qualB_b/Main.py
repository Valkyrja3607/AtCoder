n,m=[int(j) for j in input().split()]
l=[int(j) for j in input().split()]
import collections
c=collections.Counter(l)
ll=c.most_common()
if ll[0][1]>n/2:
    print(ll[0][0])
else:
    print("?")