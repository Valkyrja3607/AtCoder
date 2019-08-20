n=int(input())
b=[-1,-1]
ll=[int(i) for i in range(2,n+1)]
l1=[0 for i in range(n+1)]
l2=[[] for i in range(n+1)]
for i in range(n-1):
    p=int(input())
    b.append(p)
    if p in ll:
        ll.remove(p)
from collections import deque
q=deque(ll)
while q:
    p=q.popleft()
    l2[b[p]].append(p)
    if l2[p]==[]:
        l1[p]=1
    else:
        l3=[]
        for i in l2[p]:
            l3.append(l1[i])
        l1[p]=1+max(l3)+min(l3)
    if b[p]!=-1:
        q.append(b[p])
print(l1[1])