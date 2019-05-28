n,k=map(int,input().split())
v=[int(i) for i in input().split()]
ans=[]

for i in range(min(n,k)+1):
    for j in range(min(n,k)-i+1):
        d=k-i-j
        l=v[0:i]
        r=v[n-j:n]
        p=r+l
        q=[]
        s=sum(p)
        for x in p:
            if x<0:
                q.append(x)
        q.sort()
        for x in range(min(len(q),d)):
            s-=q[x]
        ans.append(s)
        
print(max(ans))




