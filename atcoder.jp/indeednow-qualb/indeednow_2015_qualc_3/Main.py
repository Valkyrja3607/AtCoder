n=int(input())
import heapq
q=[1]
heapq.heapify(q)
l=[[]for i in range(n+1)]
ans=[]
for i in range(n-1):
    a,b=map(int,input().split())
    l[a].append(b)
    l[b].append(a)
s=set()
while q:
    p=heapq.heappop(q)
    ans.append(p)
    s.add(p)
    for j in  l[p]:
        if j not in s:
            heapq.heappush(q,j)    
print(*ans)