import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import csgraph_from_dense
from collections import deque

n=int(input())
l=[]
ll=[]
E=[[] for i in range(n)]
# 二部グラフ判定用
V = [0 for i in range(n)]

for i in range(n):
    s=input()
    ll.append(s)
    for j in range(n):
        if s[j]=="1":
            l.append([i,j,1])
            E[i].append(j)
            E[j].append(i)

edge=np.array(l,dtype=np.int64).T
graph=csr_matrix(((edge[2],edge[:2])),(n,n))

dist_mat = floyd_warshall(graph).astype(np.int32)
 
max_d = dist_mat.max()
 
def dfs(cur, pre, col):
    stack = deque([[cur, pre, col]])
    while stack:
        cur, pre, col = stack.pop()
        if V[cur] and V[cur] != col:
            return False
        else:
            V[cur] = col
        for e in E[cur]:
            if e != pre:
                stack.append([e, cur, -1 * col])
        # 一度通った辺は通らない
        E[cur] = []
    return True
 
# 二部グラフ判定
if not dfs(0, -1, 1):
    print(-1)
    exit()

answer = max_d + 1
print(answer)

