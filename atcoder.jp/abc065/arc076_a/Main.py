import math

n,m=map(int,input().split())

if n==m:
    print((2*math.factorial(n)**2)%1000000007)
elif abs(n-m)==1:
    print((math.factorial(n)*math.factorial(m))%1000000007)
else:
    print(0)






