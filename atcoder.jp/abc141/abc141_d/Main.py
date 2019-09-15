n,m=[int(j) for j in input().split()]
a=[-int(j) for j in input().split()]
import heapq
heapq.heapify(a)
for i in range(m):
    p=heapq.heappop(a)
    p=(-p)//2
    heapq.heappush(a,-p)
print(-sum(a))