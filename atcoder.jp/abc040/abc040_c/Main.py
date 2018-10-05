n=int(input())
a=[int(i) for i in input().split()]

ans=[10000000000 for i in range(n)]

for i in range(n):
    if i==0:
        ans[i]=0
    elif i==1:
        ans[i]=ans[i-1]+abs(a[i]-a[i-1])
    else:
        ans[i]=min(ans[i-2]+abs(a[i-2]-a[i]),ans[i-1]+abs(a[i-1]-a[i]))

print(ans[-1])