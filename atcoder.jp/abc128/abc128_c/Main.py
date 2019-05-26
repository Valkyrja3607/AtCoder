n,m=map(int,input().split())
ks=[]
for i in range(m):
    ks.append([int(j) for j in input().split()])
p=[int(i) for i in input().split()]

def base(X, a):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%a)+out
        X_dumy = int(X_dumy/a)
    return str(out).rjust(n,'0')
ans=0
for x in range(2**n):
    s=[0 for _ in range(m)]
    b=base(x,2)
    for i in range(m):
        for j in range(ks[i][0]):
            if b[ks[i][j+1]-1]=="0":
                if s[i]==0:
                    s[i]=1
                else:
                    s[i]=0
    if s==p:
        ans+=1

print(ans)
    
        
    







