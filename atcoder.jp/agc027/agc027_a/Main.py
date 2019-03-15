n,x=map(int,input().split())

a=[int(i) for i in input().split()]

a.sort()
i=0
ans=0

while x>0 and i<n:
    if x-a[i]>=0:
        x-=a[i]
        ans+=1
    else:
        x=0
    if i==n-1:
        if x>0:
            ans-=1
    i+=1

print(ans)