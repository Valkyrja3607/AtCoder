n,a,b=[int(j) for j in input().split()]
print(a*(n//(a+b))+min(n%(a+b),a))