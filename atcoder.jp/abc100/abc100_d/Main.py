n,m=map(int,input().split())
l=[]
for i in range(n):
    x,y,z=map(int,input().split())
    l.append([x+y+z,x+y-z,x-y+z,-x+y+z,x-y-z,-x+y-z,-x-y+z,-x-y-z])

ans=0
from operator import itemgetter
for i in range(8):
    l.sort(key=itemgetter(i))
    l=l[::-1]
    p=0
    for j in range(m):
        p+=l[j][i]
    ans=max(ans,p)
print(ans)