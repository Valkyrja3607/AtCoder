import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
n,x=map(int,input().split())
h=np.array([int(j) for j in input().split()])
l=[]
if n==1:
    print(0)
    exit()
for i in range(n-1):
    a,b=map(int,input().split())
    l.append((a,b,1))
edge=np.array(l,dtype=np.int64).T
graph=csr_matrix(((edge[2],edge[:2]-1)),(n,n))

_,root=dijkstra(graph,directed=False,indices=x-1,return_predecessors=True)
s=set()
for i in np.where(h==1)[0]:
    q=i
    while True:
        if q==x-1:
            break
        p=root[q]
        if (p,q) in s:
            break
        s.add((p,q))
        q=p
        if p==-9999:
            break
print(len(s)*2)


