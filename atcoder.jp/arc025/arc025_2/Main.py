import numpy as np
h,w=map(int,input().split())
c=np.array([[pow(-1,idx+i)*int(j)for idx,j in enumerate(input().split())]for i in range(h)])
np.cumsum(c,out=c,axis=0)
np.cumsum(c,out=c,axis=1)
c=np.pad(c,(1,0),'constant')
ans=0
for i in range(h,0,-1):
    for j in range(w,0,-1):
        if i*j<ans:break
        t=c[i:,j:]-c[:-i,j:]-c[i:,:-j]+c[:-i,:-j]
        if (t==0).any():ans=i*j
print(ans)