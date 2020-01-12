import numpy as np
h,w=map(int,input().split())
l=set()
for i in range(h):
    t=input()
    for j in range(w):
        if t[j]==".":
            l.add((i,j))

s=set()
from collections import deque
graph=np.zeros((h*w,h*w),dtype=np.int64)
for x,y in l:
        if (x+1,y) in l and (x*w+y,(x+1)*w+y) not in s:
            graph[x*w+y,(x+1)*w+y]=1
            s.add((x*w+y,(x+1)*w+y))
        if (x,y+1) in l and (x*w+y,x*w+y+1) not in s:
            graph[x*w+y,x*w+y+1]=1
            s.add((x*w+y,x*w+y+1))

from scipy.sparse.csgraph import floyd_warshall


ans=floyd_warshall(graph,directed=False)
cond=ans!=float("inf")
print(int(ans[cond].max()))