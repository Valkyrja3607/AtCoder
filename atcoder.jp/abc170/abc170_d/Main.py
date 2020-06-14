import numpy as np
n,*a=map(int,open(0).read().split())
l=np.zeros(max(a)+1)
a.sort()
a+=[10**7]
r=0
for i,j in zip(a,a[1:]):
    if l[i]==0:
        l[::i]=1
        if i!=j:
            r+=1
print(r)