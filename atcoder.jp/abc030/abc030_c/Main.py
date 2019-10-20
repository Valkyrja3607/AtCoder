n,m=[int(j) for j in input().split()]
x,y=[int(j) for j in input().split()]
a=[int(j) for j in input().split()]
b=[int(j) for j in input().split()]
ans=0
import bisect
t=0
i=0
while True:
    if i%2==0:
        if bisect.bisect_left(a,t)!=n:
            t=a[bisect.bisect_left(a,t)]+x
        else:
            break
    else:
        if bisect.bisect_left(b,t)!=m:
            t=b[bisect.bisect_left(b,t)]+y
            ans+=1
        else:
            break
    i+=1

print(ans)
