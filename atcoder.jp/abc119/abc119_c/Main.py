n,A,B,C=map(int,input().split())

l=[]

for i in range(n):
    l.append(int(input()))

def base(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out
ans=10**9
for i in range(4**n):
    d=str(base(i,4)).rjust(n,'0')
    a=0
    b=0
    c=0
    ca=-10
    cb=-10
    cc=-10
    for j in range(n):
        if d[j]=="1":
            a+=l[j]
            ca+=10
        elif d[j]=="2":
            b+=l[j]
            cb+=10
        elif d[j]=="3":
            c+=l[j]
            cc+=10
    if ca<0:
        ca=0
    if cb<0:
        cb=0
    if cc<0:
        cc=0
    if a*b*c!=0:
        ans=min(ans,abs(A-a)+abs(B-b)+abs(C-c)+ca+cb+cc)
    
print(ans)








