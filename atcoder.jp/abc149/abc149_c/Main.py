def factorize(n):
    fct=[]
    b,e=2,0
    while b*b<=n:
        while n%b==0:
            n=n//b
            e=e+1
        if e>0:
            fct.append((b,e))
        b,e=b+1,0
    if n>1:
        fct.append((n,1))
    return fct
n=int(input())
while True:
    l=factorize(n)
    if len(l)==1 and l[0][1]==1:
        print(n)
        exit()
    else:
        n+=1