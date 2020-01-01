import sys
input=sys.stdin.readline
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

n,m=map(int,input().split())
edge=np.array([input().split() for _ in range(m)],dtype=np.int64).T
graph=csr_matrix(((edge[2],edge[:2]-1)),(n,n))

#False->無向グラフ True->有効グラフ
ans=floyd_warshall(graph,directed=False)

a=10**18
b=0

for i in ans:
    tmp=i.max()
    if a>tmp:
        a=int(tmp)
print(a)