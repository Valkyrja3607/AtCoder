n=int(input())
l=[int(j) for j in input().split()]
ans=-10**18
for i in range(n):
    T=-10**18
    A=-10**18
    for j in range(n):
        if i==j:
            continue
        t,a=0,0
        if i>j:
            x,y=j,i
        else:
            x,y=i,j
        for k in range(x,y+1):
            if k%2==x%2:
                t+=l[k]
            else:
                a+=l[k]
        if A<a:
            A=a
            T=t
    ans=max(ans,T)
print(ans)
        
        
            







