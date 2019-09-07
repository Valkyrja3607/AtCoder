n,x=map(int,input().split())
a=[int(j) for j in input().split()]
ref=[10**18]*n
ans=10**18
for i in range(n):
	ref=[min(ref[j],a[(j+i)%n]) for j in range(n)]
	ans=min(ans,sum(ref)+i*x)
print(ans)