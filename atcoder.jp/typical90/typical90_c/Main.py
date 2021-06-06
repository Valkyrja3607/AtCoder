n=int(input())
l=[[]for i in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    l[a-1].append(b-1)
    l[b-1].append(a-1)

from collections import deque
q = deque([(0,0)])
d=[0]*n
s=set()
while q:
    p,r=q.popleft()
    if p not in s:
        s.add(p)
        for i in l[p]:
            d[i]=r+1
            q.append((i,r+1))
tmp=0
start=0
for i,j in enumerate(d):
    if tmp<j:
        start=i
        tmp=j
q = deque([(start,0)])
d=[0]*n
s=set()
while q:
    p,r=q.popleft()
    if p not in s:
        s.add(p)
        for i in l[p]:
            d[i]=r+1
            q.append((i,r+1))
print(max(d)+1)