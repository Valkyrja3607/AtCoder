a,b=input().split()
s=int(a+b)
for i in range(1000):
    if i**2==s:
        print("Yes")
        exit()
print("No")
