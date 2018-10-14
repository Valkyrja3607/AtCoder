i=input()

a=int(i[0])
b=int(i[1])
c=int(i[2])
d=int(i[3])

if a+b+c+d==7:
    x="+"
    y="+"
    z="+"
elif a+b+c-d==7:
    x="+"
    y="+"
    z="-"
elif a+b-c+d==7:
    x="+"
    y="-"
    z="+"    
elif a-b+c+d==7:
    x="-"
    y="+"
    z="+"
elif a-b-c+d==7:
    x="-"
    y="-"
    z="+"
elif a-b+c-d==7:
    x="-"
    y="+"
    z="-"
elif a+b-c-d==7:
    x="+"
    y="-"
    z="-"
elif a-b-c-d==7:
    x="-"
    y="-"
    z="-"
    
    
print(a,end="")
print(x,end="")
print(b,end="")
print(y,end="")
print(c,end="")
print(z,end="")
print(d,end="")
print("=7")