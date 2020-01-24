import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

n=int(input())
a,b=[int(j)-1 for j in input().split()]
m=int(input())
xy=[]
s=set()
for i in range(m):
    p,q=[int(j)-1 for j in input().split()]
    xy.append([p,q])
    s.add((p,q))
    s.add((q,p))
xy=np.array(xy)


graph=np.zeros((n,n),dtype=np.int64)
for i,j in xy: graph[i,j]=1

l=np.array(dijkstra(graph,directed=False,indices=a),dtype=np.int64)
mod=10**9+7

ll=[[] for i in range(n)]
for i in range(n):
    ll[l[i]].append(i)

dp=[0]*(n)
dp[a]=1
for i in range(l[b]):
    for p in ll[i]:
        for q in ll[i+1]:
            if (p,q) in s or (q,p) in s:
                dp[q]+=dp[p]
                dp[q]%=mod 

print(dp[b])