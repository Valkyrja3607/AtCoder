import numpy as np
r,c=map(int,input().split())
l1=[]
l2=[]
for i in range(r):
    l=[int(j) for j in input().split()]
    l1.append(l)
    tmp=[]
    for i in l:
        if i==0:
            tmp.append(1)
        else:
            tmp.append(0)
    l2.append(tmp)
l1=np.array(l1)
l2=np.array(l2)
ans=0

for i in range(1<<r):
    b=bin(i)[2:].rjust(r,"0")
    tmp=np.zeros(c)
    ind=0
    for j in b:
        if j=="0":
            tmp+=l1[ind]
        else:
            tmp+=l2[ind]
        ind+=1
    t=np.maximum(tmp,r-tmp).sum()

    if t>ans:
        ans=t
print(int(ans))

