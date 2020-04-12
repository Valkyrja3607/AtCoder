k=int(input())

def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

ans=0
import itertools
for x in itertools.product(range(1,k+1),repeat=3):
    a,b,c=x
    ans+=gcd(gcd(a,b),c)
print(ans)
