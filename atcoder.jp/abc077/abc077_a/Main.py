a=input()
b=input()

ar=a[::-1]
br=b[::-1]

if br==a and ar==b:
    print("YES")
else:
    print("NO")