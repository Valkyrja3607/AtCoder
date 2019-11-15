k=int(input())
a,b=2,1
for i in range(k-1):
    a,b=a+b,a
print(a,b)