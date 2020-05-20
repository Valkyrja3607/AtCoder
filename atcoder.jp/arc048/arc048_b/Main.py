n=int(input())
import numpy as np
rh=np.array([[int(j)for j in input().split()]for i in range(n)])
r=rh[:,0]
h=rh[:,1]
rg=r[h==1]
rc=r[h==2]
rp=r[h==3]
g=np.bincount(rg,minlength=100001)
c=np.bincount(rc,minlength=100001)
p=np.bincount(rp,minlength=100001)
cum=(g+c+p).cumsum()

win=cum[r-1]
draw=np.zeros_like(win)
win[h==1]+=c[rg]
win[h==2]+=p[rc]
win[h==3]+=g[rp]
draw[h==1]+=g[rg]
draw[h==2]+=c[rc]
draw[h==3]+=p[rp]
draw-=1
lose=n-win-draw-1
for w,l,d in zip(win,lose,draw):
    print(w,l,d)