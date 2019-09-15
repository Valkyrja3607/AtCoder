n=int(input())
a=[int(j) for j in input().split()]

tmp=1
ans=0
for i in range(n-1):
    if a[i]<a[i+1]:
        tmp+=1
    else:
        ans+=tmp*(tmp+1)//2
        tmp=1
ans+=tmp*(tmp+1)//2
print(ans)