n,k=map(int,input().split())
p=[int(j)-1 for j in input().split()]
c=list(map(int,input().split()))
l=[[]]
from collections import deque
q = deque(list(range(n)))
s=set()
while q:
    i=q.popleft()
    if i not in s:
        l[-1].append(c[i])
        q.appendleft(p[i])
        s.add(i)
    elif l[-1]!=[]:
        l.append([])
ans=-10**18
for ll in l:
    m=len(ll)
    if m==0:continue
    p=k%m
    s=sum(ll)
    for i in range(m):
        tmp=0
        for j in range(min(m,k)):
            idx=(i+j)%m
            tmp+=ll[idx]
            if j<p and s>0:
                ans=max(ans,s*(k//m)+tmp)
            elif s>0 and k//m>0:
                ans=max(ans,s*(k//m-1)+tmp)
            ans=max(ans,tmp)
print(ans)