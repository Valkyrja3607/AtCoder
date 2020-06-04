n=int(input())
s=list(input())
ans=0
import collections
c=collections.Counter(s)
for i in c:
    ans+=c[i]%2
print(ans)