def gcd(a, b):

	while b:

		a, b = b, a % b

	return a

n,xs=map(int,input().split())

x=[abs(int(i)-xs) for i in input().split()]

ans=x[0]
for i in range(n):
    ans=gcd(ans,x[i])

print(ans)