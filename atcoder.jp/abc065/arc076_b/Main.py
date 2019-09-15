n=int(input())
lx=[]
ly=[]
for i in range(n):
    x,y=[int(j) for j in input().split()]
    lx.append((i,x,y))
    ly.append((i,x,y))
from operator import itemgetter
lx.sort(key=itemgetter(1))
ly.sort(key=itemgetter(2))
# 最小全域木
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
edge=set()
for i in range(n-1):
    i1,x1,y1=lx[i]
    i2,x2,y2=lx[i+1]
    d=min(abs(x1-x2),abs(y1-y2))
    edge.add((i1,i2,d))
for i in range(n-1):
    i1,x1,y1=ly[i]
    i2,x2,y2=ly[i+1]
    d=min(abs(x1-x2),abs(y1-y2))
    edge.add((i1,i2,d))
row,col,value = zip(*edge)
value = np.array(value,dtype=int)
graph = csr_matrix((value,(row,col)),shape=(n,n))

tree = minimum_spanning_tree(graph,overwrite = True).astype(int)
print(tree.sum())
