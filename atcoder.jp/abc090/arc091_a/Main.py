n,m=map(int,input().split())

if n>2:
    n-=2
if m>2:
    m-=2
if n==2 or m==2:
    print(0)
else:
    print(n*m)
    