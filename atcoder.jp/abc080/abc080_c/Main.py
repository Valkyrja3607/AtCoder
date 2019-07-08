n=int(input())
f=[]
p=[]
for i in range(n):
    q=[int(j) for j in input().split()]
    f.append(q)
for i in range(n):
    q=[int(j) for j in input().split()]
    p.append(q)

def base(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out.rjust(10,'0')
ans=-10**100
for i in range(1,1024):
    i=base(i,2)
    res=0
    for j in range(n):
        c=0
        for k in range(10):
            if f[j][k]==1 and int(i[k])==1:
                c+=1
        res+=p[j][c]
    ans=max(ans,res)
print(ans)

    


