n,k=map(int,input().split())
a=[int(input())for i in range(k)]
a.sort()
ans,tmp=0,1
if a[0]:
    for i,j in zip(a,a[1:]):
        if i+1==j:
            tmp+=1
            ans=max(ans,tmp)
        else:
            tmp=0
else:
    l=[]
    for i,j in zip(a[1:],a[2:]):
        if i+1==j:
            tmp+=1
        else:
            l.append(tmp)
            tmp=1
    l.append(tmp)
    for i,j in zip(l,l[1:]):
        ans=max(ans,i+j)
print(ans+1)