n,k=map(int,input().split())
x=[int(i) for i in input().split()]
ans=100000000000000

if x[0]*x[-1]>0:
    if x[0]>0:
        ans=x[k-1]
    elif x[0]<0:
        ans=abs(x[-k])
else:
    for i in range(n-k+1):
        if x[i]*x[i+k-1]<=0:
            ans=min(abs(x[i])+abs(x[i+k-1])+min(abs(x[i]),abs(x[i+k-1])),ans)
print(ans)