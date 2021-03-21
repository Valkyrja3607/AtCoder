n=int(input())
ans=[2]*(n+1)
ans[1]=1
for i in range(2,1+n):
    t=2
    while t<=i**0.5:
        if i%t==0:
            ans[i]=ans[i//t]+1
            break
        t+=1
print(*ans[1:])