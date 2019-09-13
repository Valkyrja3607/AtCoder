n=int(input())
a=[int(j) for j in input().split()]
a.sort()

tmp=0
ans=n
c=1
for i in range(n-1):
    tmp+=a[i]
    if tmp*2<a[i+1]:
        ans-=c
        c=1
    else:
        c+=1
print(ans)