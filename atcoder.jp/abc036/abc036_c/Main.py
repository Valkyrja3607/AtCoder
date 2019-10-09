n=int(input())
a=[(int(input()),i) for i in range(n)]
a.sort()
ans=[0]*n
b=0
a+=[(10**18,10**18)]
for i in range(n):
    ans[a[i][1]]=b
    if a[i][0]!=a[i+1][0]:
        b+=1
print(*ans)