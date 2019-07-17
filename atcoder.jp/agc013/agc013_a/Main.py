n=int(input())
a=[int(j) for j in input().split()]
ans=1
p=2
for i in range(1,n):
    if a[i-1]<a[i]:
        if p==0:
            continue
        if p==2:
            p=0
        else:
            p=2
            ans+=1
    elif a[i-1]>a[i]:
        if p==1:
            continue
        if p==2:
            p=1
        else:
            p=2
            ans+=1

    
print(ans)