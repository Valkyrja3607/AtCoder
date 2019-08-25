a,b,c=[int(j) for j in input().split()]
k=int(input())
print(a+b+c-max(a,b,c)+max(a,b,c)*2**k)