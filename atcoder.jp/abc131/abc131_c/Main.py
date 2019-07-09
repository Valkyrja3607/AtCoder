a,b,c,d=map(int,input().split())
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

def lcm(x,y):
    return x*y//gcd(x,y)
p=lcm(c,d)
def f(n):
    return b//n-(a-1)//n
ans=b-a+1-f(c)-f(d)+f(p)
print(ans)
