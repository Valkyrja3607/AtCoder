n,k=map(int,input().split())
def base(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out

l=[[int(j) for j in input().split()] for i in range(n)]

for i in range(k**n):
    b=base(i,k).rjust(n,"0")
    t=0
    c=0
    for j in b:
        j=l[c][int(j)]
        t^=j
        c+=1
    if t==0:
        print("Found")
        exit()

print("Nothing")

