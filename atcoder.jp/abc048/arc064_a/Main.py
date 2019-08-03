n,x=map(int,input().split())
a=[int(i) for i in input().split()]
ans=0
for i in range(1,n):
    if a[i-1]+a[i]<=x:
        continue
    else:
        tmp=a[i-1]+a[i]-x
        ans+=tmp
        if tmp<=a[i]:
            a[i]-=tmp
        else:
            a[i]=0
            a[i-1]-=tmp-a[i]
print(ans)

