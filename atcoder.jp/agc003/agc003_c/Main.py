n=int(input())
a=[int(input())for i in range(n)]
b=a.copy()
b.sort()
ans=0
import bisect
for i,j in enumerate(a):
    k=bisect.bisect_left(b,j)
    if i%2!=k%2:
        ans+=1

print(ans//2)