n,m=[int(j)for j in input().split()]
l=[[]for i in range(n+1)]
for i in range(m):
    a,b=[int(j)for j in input().split()]
    l[a].append(b)
    l[b].append(a)
ans=[0]*(n+1)
from collections import deque
q=deque([1])
s=set([1])
while q:
    i=q.popleft()
    for k in l[i]:
        if k not in s:
            ans[k]=i
            q.append(k)
            s.add(k)

if 0 not in ans[2:]:
    print("Yes")
    print('\n'.join(map(str,ans[2:])))
else:
    print("No")