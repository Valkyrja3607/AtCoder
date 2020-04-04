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
ans=set(make_divisors(n-1))
for k in make_divisors(n)[1:]:
    if k==1:
        continue
    m=n
    while m>=k:
        if m%k==0:
            m=m//k
        else:
            m=m%k
    if m==1:
        ans.add(k)
print(len(ans)-1)