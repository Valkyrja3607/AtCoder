n,m=map(int,input().split())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    divisors.reverse()
    return divisors

l=make_divisors(m)

for i in l:
    if i*n<=m:
        print(i)
        import sys
        sys.exit()
