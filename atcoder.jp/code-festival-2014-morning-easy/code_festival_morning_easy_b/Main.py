n=int(input())
n%=40
if n>20:
    print(41-n)
elif n==0:
    print(1)
else:
    print(n)