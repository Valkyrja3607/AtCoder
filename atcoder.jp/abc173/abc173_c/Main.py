h,w,K=map(int,input().split())
s=[list(input())for i in range(h)]
import numpy as np
s=np.array(s)
l=[]
for i in range(h):
    l.append(len(s[i][s[i]=="#"]))
for i in range(w):
    l.append(len(s[:,i][s[:,i]=="#"]))
ss=sum(l)//2
n=h+w
ans=0
for i in range(1<<n):
    tmp=ss
    for j in range(h):
        if i>>j&1:
            tmp-=l[j]
    for j in range(h,n):
        if i>>j&1:
            tmp-=l[j]
            for idx,k in enumerate(s[:,j-h]):
                if k=="#":
                    if i>>idx&1:
                        tmp+=1
    if tmp==K:
        ans+=1
print(ans)