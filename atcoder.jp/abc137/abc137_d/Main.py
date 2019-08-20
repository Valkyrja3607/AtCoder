n,m=map(int,input().split())
ab=[]
l=[[] for i in range(m+1)]
for i in range(n):
    tmp=[int(j) for j in input().split()]
    ab.append(tmp)
    a,b=tmp
    if a<=m:
        l[a].append(b)
import heapq
q=[]
ans=0
for i in range(1,1+m):
    for j in l[i]:
        heapq.heappush(q,-j)
    if q:
        ans-=heapq.heappop(q)
print(ans)