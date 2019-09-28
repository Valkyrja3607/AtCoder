n=int(input())
if n%2==0:
    print(0.5)
elif n==1:
    print(1.0)
else:
    print((n//2+1)/n)