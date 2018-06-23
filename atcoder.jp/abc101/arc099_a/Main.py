import math

n,k=map(int,input().split())

a=[int(i) for i in input().split()]

l=(n-1)/(k-1)

m=math.ceil(l)

print(m)