n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))

#最大公約数
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

#最小公倍数
def lcm(x,y):
    return x*y//gcd(x,y)

ans=a[0]
for i in a:
    ans=lcm(ans,i)
    
print(ans)