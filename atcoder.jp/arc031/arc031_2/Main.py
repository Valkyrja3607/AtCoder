a=[]
l=set()
ll=[]
t,u=0,0
for i in range(10):
    s=input()
    a.append(s)
    for j in range(10):
        if s[j]=="x":
            ll.append((i,j))
        else:
            l.add((i,j))
            t,u=i,j
m=[[0]*10 for i in range(10)]
c=1
from collections import deque
q=deque([(t,u)])
m[t][u]=c
l.remove((t,u))
while l or q:
    if q:
        i,j=q.popleft()
        if (i-1,j) in l:
            q.append((i-1,j))
            m[i-1][j]=c
            l.remove((i-1,j))
        if (i,j-1) in l:
            q.append((i,j-1))
            l.remove((i,j-1))
            m[i][j-1]=c
        if (i+1,j) in l:
            q.append((i+1,j))
            l.remove((i+1,j))
            m[i+1][j]=c
        if (i,j+1) in l:
            q.append((i,j+1))
            l.remove((i,j+1))
            m[i][j+1]=c
    else:
        c+=1
        for i,j in l:
            m[i][j]=c
            q.append((i,j))
            l.remove((i,j))
            break
for i,j in ll:
    tmp=list(range(1,c+1))
    if 0<=i-1:
        if m[i-1][j] in tmp:
            tmp.remove(m[i-1][j])
    if i+1<=9:
        if m[i+1][j] in tmp:
            tmp.remove(m[i+1][j])
    if 0<=j-1:
        if m[i][j-1] in tmp:
            tmp.remove(m[i][j-1])
    if j+1<=9:
        if m[i][j+1] in tmp:
            tmp.remove(m[i][j+1])
    if not tmp:
        print("YES")
        exit()

print("NO")



