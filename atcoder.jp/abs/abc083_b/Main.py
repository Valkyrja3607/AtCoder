n,a,b=map(int,input().split())
c=0

for x in range(1,n+1):
    l=[int(L) for L in list(str(x))]
    s=sum(l)
    if a<=s<=b:
        c += x

print(c)