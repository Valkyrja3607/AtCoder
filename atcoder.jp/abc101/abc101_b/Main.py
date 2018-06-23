n=int(input())

a=[int(i) for i in list(str(n))]

s=sum(a)

if n%s==0:
    print("Yes")
else:
    print("No")