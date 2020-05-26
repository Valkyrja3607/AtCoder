h,w=map(int,input().split())
c=[]
for i in range(h):
    s=input()
    for j,k in enumerate(s):
        if k=="s":
            si,sj=i,j
    c.append(list(s))
from collections import deque
dq=deque([(si,sj)])
dp=deque()
ans=0
import copy
while dq and ans<=2:
    i,j=dq.popleft()
    for p,q in [[-1,0],[1,0],[0,1],[0,-1]]:
        x,y=i+p,j+q
        if 0<=x<h and 0<=y<w:
            if c[x][y]==".":
                c[x][y]=ans
                dq.append((x,y))
            elif c[x][y]=="#":
                c[x][y]=ans+1
                dp.append((x,y))
            elif c[x][y]=="g":
                if ans<=2:
                    print("YES")
                else:
                    print("NO")
                exit()
    if not dq:
        ans+=1
        dq=copy.deepcopy(dp)
        dp=deque()
print("NO")