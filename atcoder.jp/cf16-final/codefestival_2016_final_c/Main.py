import numpy as np;from scipy.sparse import *;l=[];n,m=map(int,input().split())
for i in range(n):
  for j in input().split()[1:]:l.append((i,int(j)+n-1,1))
edge=np.array(l,dtype=np.int64).T;graph=csr_matrix(((edge[2],edge[:2])),(n+m,n+m));_,l=csgraph.connected_components(graph);print("NO"if 1 in l[:n]else"YES")