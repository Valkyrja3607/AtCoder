n,q=map(int,input().split())
f=[set() for i in range(n+1)]
ff=[set() for i in range(n+1)]
for i in range(q):
    s=input()
    if s[0]=="1":
        a,b,c=map(int,s.split())
        f[b].add(c)
        ff[c].add(b)
    elif s[0]=="2":
        a,b=map(int,s.split())
        for j in list(ff[b]):
            f[b].add(j)
            ff[j].add(b)
    else:
        a,b=map(int,s.split())
        for j in list(f[b]):
            for k in list(f[j]):
                f[b].add(k)
                ff[k].add(b)
        
for i in range(1,1+n):
    s=["N"]*n
    for j in f[i]:
        s[j-1]="Y"
    s[i-1]="N"
    print("".join(s))