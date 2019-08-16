n,W=map(int,input().split())
vw=[[int(j) for j in input().split()] for i in range(n)]
v,w=zip(*vw)
 
def case1():
  left=[(0,0)]
  right=[(0,0)]
  for i in range(n//2):
    left+=[(x+w[i],y+v[i]) for x,y in left]
  for i in range(n//2,n):
    right+=[(x+w[i],y+v[i]) for x,y in right]
  left.sort()
  right.sort()
  def remove_worthless(li):
    temp=[]
    current_value=-1
    for w,v in li:
      if w>W:
        break
      if v>current_value:
        current_value=v
        temp.append((w,v))
    return temp
  left=remove_worthless(left)
  right=remove_worthless(right)
  INF=10**18
  right.append((INF,0))
  j=0
  x=0
  for wL,vL in left[::-1]:
    wR_max=W-wL
    while right[j+1][0] <= wR_max:
      j+=1
    vLR=vL+right[j][1]
    if x<vLR:
      x=vLR
  return x
    
def case2():
  import numpy as np
  L=n*1000+1
  dp=np.zeros(L,dtype=np.int64)
  nn=1
  for v,w in vw:
    dp[w:w+nn]=np.maximum(dp[w:w+nn],dp[:nn] + v)
    nn+=w
  return dp[:W+1].max()
 
def case3():
  import numpy as np
  L=n*1000+1
  dp=np.zeros(L,dtype=np.int64)
  dp[1:]=10**18
  nn=1
  for v,w in vw:
    dp[v:v+nn]=np.minimum(dp[v:v+nn],dp[:nn] + w)
    nn+=v
  possible_value=(dp<=W).nonzero()[0]
  return possible_value.max()
 
if n<=30:
  print(case1())
elif max(w)<=1000:
  print(case2())
else:
  print(case3())