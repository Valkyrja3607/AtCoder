n=int(input())
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

l=make_divisors(n)
m=len(l)
ans=10**100
for i in range(min(m//2+1,m)):
    a,b=len(str(l[i])),len(str(n//l[i]))
    ans=min(ans,max(a,b))
print(ans)

