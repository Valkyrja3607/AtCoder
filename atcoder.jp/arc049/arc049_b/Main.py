n=int(input())
l=[list(map(int,input().split()))for i in range(n)]
import numpy as np
l=np.array(l)
x=l[:,0]
y=l[:,1]
c=l[:,2]
def f(t):
    k=t/c
    x_l=(x-k).max()
    x_r=(x+k).min()
    y_l=(y-k).max()
    y_r=(y+k).min()
    if x_l<=x_r and y_l<=y_r:
        return True
    return False
left=0
right=10**15
while right-left>0.0000001:
    mid=(left+right)/2
    if f(mid):
        right=mid
    else:
        left=mid
print(right)