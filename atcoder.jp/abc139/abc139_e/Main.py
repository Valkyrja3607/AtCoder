n=int(input())
a=[]
l=[[] for i in range(n)]
ind=[0 for i in range(n)]
s=set()
ans=1
from collections import deque
q=deque([])
for i in range(n):
    tmp=[int(j)-1 for j in input().split()]
    a.append(tmp)
    for j in tmp:
        if i<j:
            l[i].append((i,j))
        else:
            l[i].append((j,i))
    q.append(l[i][0])
ll=[]
while q:
    p=q.popleft()
    if p in s:
        s.remove(p)
        i,j=p
        if i in ll or j in ll:
            ans+=1
            ll=[i,j]
        else:
            ll.append(i)
            ll.append(j)
        if ind[i]<n-2:
            ind[i]+=1
            q.append(l[i][ind[i]])
        if ind[j]<n-2:
            ind[j]+=1
            q.append(l[j][ind[j]])
    else:
        s.add(p)

for i in range(n):
    if ind[i]!=n-2:
        print(-1)
        exit()
print(ans)




