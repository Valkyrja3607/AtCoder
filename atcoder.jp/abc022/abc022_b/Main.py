n=int(input())
a=[int(input())for i in range(n)]
import collections
c=collections.Counter(a)
ans=0
for i in c:
    ans+=c[i]-1
print(ans)