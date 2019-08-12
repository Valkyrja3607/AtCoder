n,k=map(int,input().split())
wp=[]
for i in range(n):
    wp.append([int(j) for j in input().split()])
from operator import itemgetter
def f(m):
    l=[]
    for i in range(n):
        l.append([wp[i][0]*(wp[i][1]-m)/100,wp[i][0],wp[i][1]])
    l.sort(key=itemgetter(0))
    l.reverse()
    s=0
    p=0
    q=0
    for i in range(k):
        s+=l[i][0]
        p+=l[i][1]
        q+=l[i][1]*l[i][2]/100
    if s>=0:
        return q/p*100
    else:
        return False


left=0.0
right=100.0
while right-left>0.001:
    mid=(left+right)/2
    if f(mid):
        left=mid
    else:
        right=mid

print(f(left))