s=input()
l=len(s)
def base(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out.rjust(l-1,'0')
ans=0
for i in range(2**(l-1)):
    b=base(i,2)
    p=1
    ans+=int(s[-1])
    for j in range(1,l):
        if b[-j]=="0":
            p*=10
            ans+=int(s[-j-1])*p
        else:
            p=1
            ans+=int(s[-j-1])

print(ans)