a=input().split()

if a[0]=="A":
    x=10
elif a[0]=="B":
    x=11
elif a[0]=="C":
    x=12
elif a[0]=="D":
    x=13
elif a[0]=="E":
    x=14
elif a[0]=="F":
    x=15

if a[1]=="A":
    y=10
elif a[1]=="B":
    y=11
elif a[1]=="C":
    y=12
elif a[1]=="D":
    y=13
elif a[1]=="E":
    y=14
elif a[1]=="F":
    y=15

if x<y:
    print("<")
elif x>y:
    print(">")
else:
    print("=")
    


