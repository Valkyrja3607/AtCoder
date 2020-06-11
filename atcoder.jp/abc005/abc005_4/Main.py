n=int(input())
d=[[int(j)for j in input().split()]for i in range(n)]
q=int(input())

l=[0]
def ruiseki(a):
    for i in range(len(a)):
        l.append(l[i]+a[i])
    del l[0]

#二乗累積和
#(a,b)->l[a-1][a-1]+l[b][b]-l[a-1][b]-l[b][a-1]
def ruiseki(a):
    l=[0]
    for i in range(len(a)):
        l.append(l[i]+a[i])
    del l[0]
    return l
l=[]
def niruiseki(a):
    l.append(ruiseki(a[0]))
    for i in range(1,len(a)):
        p=[l[i-1][0]+a[i][0]]
        q=[a[i][0]]
        for j in range(1,len(a[i])):
            q.append(q[j-1]+a[i][j])
            p.append(q[j]+l[i-1][j])
        l.append(p+[0])
niruiseki(d)
l[0]+=[0]
l.append([0]*(n+1))
from collections import defaultdict
c=defaultdict(int)
import itertools
for x1,x2 in itertools.combinations_with_replacement(range(n),2):
    for y1,y2 in itertools.combinations_with_replacement(range(n),2):
        c[(x2-x1+1)*(y2-y1+1)]=max(c[(x2-x1+1)*(y2-y1+1)],l[x2][y2]-l[x2][y1-1]-l[x1-1][y2]+l[x1-1][y1-1])
ans=[0]
for i in range(1,n*n+1):
    ans.append(max(ans[-1],c[i]))
for _ in range(q):
    print(ans[int(input())])