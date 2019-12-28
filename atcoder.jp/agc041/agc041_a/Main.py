n,a,b=[int(j) for j in input().split()]

if abs(a-b)%2==0:
    print(abs(a-b)//2)
else:
    print(min(a-1,n-b)+1+(b-a-1)//2)