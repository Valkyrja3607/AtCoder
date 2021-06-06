h,w=map(int,input().split())
a=[list(map(int,input().split()))for i in range(h)]

y=[0]*h
t=[0]*w
for i in range(h):
    for j in range(w):
        t[j]+=a[i][j]
        y[i]+=a[i][j]
for i in range(h):
    ans=[0]*w
    for j in range(w):
        ans[j]=y[i]+t[j]-a[i][j]
    print(*ans)