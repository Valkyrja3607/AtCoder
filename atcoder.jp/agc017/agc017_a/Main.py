n,p=map(int,input().split())
a=[int(i)%2 for i in input().split()]

c0=a.count(0)
c1=n-c0

def c(n,m):
    import math
    if n-m<0:
        return 0
    return(math.factorial(n)//math.factorial(n-m)//math.factorial(m))

q=0
for i in range(c0+1):
    q+=c(c0,i)


i=p
ans=0
while i<=c1:
    ans+=c(c1,i)*q
    i+=2
print(ans)