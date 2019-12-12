import numpy as np
c=np.array([input().split() for i in range(4)])
ans=np.rot90(np.rot90(c))
for i in range(4):
    print(*ans[i])