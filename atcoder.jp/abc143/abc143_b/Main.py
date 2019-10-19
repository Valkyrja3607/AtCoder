n=int(input())
d=[int(i) for i in input().split()]
ans=0
import itertools
for i,j in itertools.combinations(d,2):
    ans+=i*j
print(ans)
