a,b=[int(j) for j in input().split()]
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors
la=set(make_divisors(a))
lb=set(make_divisors(b))
l=list(la&lb)
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

ans=0
ll=set([1])
l.sort()
for i in l:
    if i==1:
        continue
    if set(make_divisors(i))&ll=={1}:
        ll.add(i)
print(len(ll))