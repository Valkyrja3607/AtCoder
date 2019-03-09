n,m,c=map(int,input().split())
b=[int(i) for i in input().split()]
a=[]
ans=0
for i in range(n):
    a=[int(j) for j in input().split()]
    p=c
    for k in range(m):
        p+=a[k]*b[k]
    if p>0:
        ans+=1
    
print(ans)


