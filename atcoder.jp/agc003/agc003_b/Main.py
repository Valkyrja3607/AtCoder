n=int(input())
l=[int(input()) for i in range(n)]
ans=0
for i in range(len(l)-1):
    ans+=l[i]//2
    l[i]=l[i]%2
    tmp=min(l[i],l[i+1])
    ans+=tmp
    l[i+1]-=tmp
ans+=l[-1]//2
print(ans)