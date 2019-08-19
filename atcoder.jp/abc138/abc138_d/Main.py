from collections import deque
n,q=map(int, input().split())
l=[[] for i in range(n+1)]
ans=[0]*(n+1)

for i in range(n-1):
    a,b=[int(j) for j in input().split()]
    l[a].append(b)
    l[b].append(a)
for i in range(q):
    p,x=[int(j) for j in input().split()]
    ans[p]+=x

que=deque()
que.append(1)
ll=[0]*(n+1)
while que:
    y=que.popleft()
    ll[y]=1
    for i in l[y]:
        if ll[i]==1:
            continue
        ans[i]+=ans[y]
        que.append(i)
print(*ans[1:])