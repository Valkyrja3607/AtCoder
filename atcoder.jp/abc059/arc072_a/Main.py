n=int(input())
a=[int(i) for i in input().split()]

if a[0]>=0:
    f=1
else:
    f=-1

s=0
ans=0
for i in range(n):
    s+=a[i]
    if s*f<0:
        ans+=abs(s)+1
        s=f
    elif s==0:
        ans+=1
        s=f
    f*=-1


if a[0]>=0:
    f=-1
else:
    f=1
s=0
ans2=0
for i in range(n):
    s+=a[i]
    if s*f<0:
        ans2+=abs(s)+1
        s=f
    elif s==0:
        ans2+=1
        s=f
    f*=-1
    
print(min(ans,ans2))
        




