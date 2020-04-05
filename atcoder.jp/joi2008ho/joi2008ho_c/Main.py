import numpy as np
n,m=map(int,input().split())
l=np.array([0]+[int(input()) for i in range(n)])
ll=(l[:,None]+l[None,:]).flatten()
l=l[l<=m]
ll=ll[ll<=m]
l.sort()
ll.sort()
ans=max(l.max(),ll.max())
idx=np.searchsorted(l,m-ll,side="right")-1
ans=max(ans,np.max(ll+l[idx]))
idx=np.searchsorted(ll,m-ll,side="right")-1
ans=max(ans,np.max(ll+ll[idx]))
print(ans)