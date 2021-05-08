n=int(input())
a=list(map(int,input().split()))
l=[i%200 for i in a]
import collections
c=collections.Counter(l)
ll=c.most_common()
ans=0
for i,j in ll:
    ans+=j*(j-1)//2
print(ans)