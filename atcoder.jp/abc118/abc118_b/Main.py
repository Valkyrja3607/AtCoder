n,m=map(int,input().split())
a=[]
for i in range(n):
    p=[int(j) for j in input().split()]
    for j in p[1:]:
        a.append(j)
ans=0
import collections
c=collections.Counter(a)
for i,j in c.most_common():
    if j==n:
        ans+=1
print(ans)

