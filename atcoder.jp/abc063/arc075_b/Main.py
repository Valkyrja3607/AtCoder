n,a,b=[int(j) for j in input().split()]
s=a-b
h=[]
for i in range(n):
    p=int(input())
    h.append(p)
h.sort()
import bisect
import math
def f(m):
    n=bisect.bisect_right(h,m*b)
    l=h[n:]
    c=0
    for i in range(len(l)):
        if l[i]-m*b/s>0:
            c+=math.ceil((l[i]-m*b)/s)
    if c<=m:
        return True
    else:
        return False
        


left=0
right=10**15
while right-left>1:
    mid=(left+right)//2
    if f(mid):
        right=mid   #ここがleftならansもleft。
    else:
        left=mid
print(right)
