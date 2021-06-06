n,m=map(int,input().split())
l=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    l[a-1].append(b-1)

ans=set()
from collections import deque
for i in range(n):
    ans.add((i,i))
    q=deque([i])
    s=set()
    while q:
        p=q.popleft()
        for j in l[p]:
            if j not in s:
                ans.add((i,j))
                q.append(j)
                s.add(j)
print(len(ans))



