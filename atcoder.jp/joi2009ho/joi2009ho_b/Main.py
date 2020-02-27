d=int(input())
n=int(input())
m=int(input())
l=[0]+[int(input()) for i in range(n-1)]
l.append(d)
l.sort()
l=[-10**18]+l+[10**18]
k=[int(input()) for i in range(m)]
ans=0
import bisect
for i in k:
    j=bisect.bisect_left(l,i)
    ans+=min(abs(l[j]-i),abs(i-l[j-1]))
print(ans)


