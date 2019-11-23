h,w,k=[int(j) for j in input().split()]
s=[input() for i in range(h)]
ans=[[0]*w for i in range(h)]
p=1

for i in range(h):
    q=0
    for j in range(w):
        if s[i][j]=="#":
            q+=1
            p+=1
            if q==1:
                p-=1
        ans[i][j]=p
    if q==0:
        for j in range(w):
            ans[i][j]=-1
    if q==1:
        for j in range(w):
            ans[i][j]=ans[i][0]
    p+=1

p=1
q=1
a=[[0 for i in range(w)] for i in range(h)]
for i in range(h):
    if ans[i][0]==-1:
        continue
    for j in range(w):
        if q!=ans[i][j]:
            p+=1
        q=ans[i][j]
        a[i][j]=p

for i in range(h):
    if a[i][0]==0 and i!=0:
        for j in range(w):
            a[i][j]=a[i-1][j]
for i in range(h)[::-1]:
    if a[i][0]==0 and i!=h-1:
        for j in range(w):
            a[i][j]=a[i+1][j]

if a[0][0]!=1:
    p=a[0][0]-1
    for i in range(h):
        for j in range(w):
            a[i][j]-=p
for i in a:
    print(*i)
