a=int(input())

b=int(a/7)
c=int(a/4)
k=0

for i in range(b+1):
    for j in range(c+1):
        if 7*i+4*j==a:
            k=1
if k==1:
    print("Yes")
else:
    print("No")