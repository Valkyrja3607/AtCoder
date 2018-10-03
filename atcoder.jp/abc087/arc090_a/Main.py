n=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]

x=[]
y=[]

for i in range(n):
    if i==0:
        x.append(a[i])
        y.append(b[i])
    else:
        x.append(x[-1]+a[i])
        y.append(y[-1]+b[i])

ans=0

for i in range(n):
    if i==0:
        ans=max(ans,x[i]+y[-1])
    else:
        ans=max(ans,x[i]+y[-1]-y[i-1])

print(ans)

    