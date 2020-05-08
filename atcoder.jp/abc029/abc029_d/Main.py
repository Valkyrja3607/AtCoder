n,a=int(input()),0
for i in range(1,10):a+=((n+1)//(10**i))*10**(i-1)+min(max(0,(n+1)%(10**i)-10**(i-1)),10**(i-1))
print(a)