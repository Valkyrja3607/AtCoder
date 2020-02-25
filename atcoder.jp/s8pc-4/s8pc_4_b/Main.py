n,k=map(int,input().split())
a=[int(j) for j in input().split()]
ans=10**100

for i in range(1<<(n-1)):
    p,q,tmp=1,0,a[0]
    for j in range(n-1):
        if tmp<a[j+1]:
            p+=1
            tmp=a[j+1]
            continue
        if i&(1<<j):
            q+=tmp-a[j+1]+1
            p+=1
            tmp+=1
    if p>=k:
        if ans>q:
            ans=q

print(ans)

