n,k=map(int,input().split())
h=[]
for i in range(n):
    h.append(int(input()))
h.sort()
mm=h[k-1]
m=h[0]
ans=mm-m
for i in range(1,n-k+1):
    mm=h[k+i-1]
    m=h[i]
    ans=min(ans,mm-m)
print(ans)




