import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

n,m,t=map(int,input().split())  #頂点数n 辺の数m
l=[int(j) for j in input().split()]
inp=[]
inp2=[]
for i in range(m):
    a,b,c=[int(j) for j in input().split()]
    inp.append((a,b,c))
    inp2.append((b,a,c))
edge=np.array(inp,dtype=np.int64).T
graph=csr_matrix(((edge[2],edge[:2]-1)),(n,n))

edge=np.array(inp2,dtype=np.int64).T
graph2=csr_matrix(((edge[2],edge[:2]-1)),(n,n))


#False->無向グラフ True->有効グラフ indives->スタートノード-1　return_predecessors=Trueを追加すると経路もでる
p=dijkstra(graph,directed=True,indices=0)
q=dijkstra(graph2,directed=True,indices=0)
ans=0

for i in range(n):
    if t-p[i]-q[i]>0:
        ans=max(ans,(t-p[i]-q[i])*l[i])

print(int(ans))






