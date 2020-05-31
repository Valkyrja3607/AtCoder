n=int(input())
import numpy as np
ab=np.array([[int(j)for j in input().split()]for i in range(n)])
a=np.median(ab[:,0])
b=np.median(ab[:,1])
if n%2:
    print(int(b-a+1))
else:
    print(int(2*b-2*a+1))