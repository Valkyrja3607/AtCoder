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
ans=10**18
for i in l:
    j=n//i
    ans=min(ans,i+j-2)
print(ans)