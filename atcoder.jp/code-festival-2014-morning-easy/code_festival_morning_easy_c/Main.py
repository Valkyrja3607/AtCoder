import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

n,m=map(int,input().split())
s,t=map(int,input().split())
edge=np.array([input().split() for _ in range(m)],dtype=np.int64).T
graph=csr_matrix(((edge[2],edge[:2]-1)),(n,n))

#False->無向グラフ True->有効グラフ indives->スタートノード-1　return_predecessors=Trueを追加すると経路もでる
su=dijkstra(graph,directed=False,indices=s-1)
ut=dijkstra(graph,directed=False,indices=t-1)
for i in range(n):
    if su[i]==ut[i] and su[i]!=float("inf"):
        print(int(i+1))
        exit()
print(-1)