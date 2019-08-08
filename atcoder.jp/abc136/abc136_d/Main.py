s=input()
s=s.replace("RL","P")
ans=[]
cr=0
cl=0

import math
for i in s:
    if i=="R":
        ans.append(0)
        cr+=1
    elif i=="L":
        ans.append(0)
    else:
        ans.append(1+cr//2)
        ans.append(1+math.ceil(cr/2))
        cr=0
k=0

for i in range(1,1+len(s)):
    if s[-i]=="L":
        cl+=1
    elif s[-i]=="P":
        ans[-i-k]+=cl//2
        k+=1
        ans[-i-k]+=math.ceil(cl/2)
        cl=0

for i in range(len(ans)):
    if i!=len(ans)-1:
        print(ans[i],end=" ")
    else:
        print(ans[i])