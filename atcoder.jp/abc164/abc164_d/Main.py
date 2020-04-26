s=[int(j) for j in input()][::-1]
c=[0]*2019
tmp=0
c[0]+=1
t=1
import numpy as np
for i in s:
    tmp+=t*i
    c[tmp%2019]+=1
    t=t*10%2019
c=np.array(c)
ans=c*(c-1)//2
print(ans.sum())