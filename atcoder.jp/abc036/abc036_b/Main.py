n=int(input())
import numpy as np
c=[]
for i in range(n):
    c.append(list(input()))
ans=np.rot90(np.rot90(np.rot90(np.array(c))))
for i in ans:
    print("".join(i)) 