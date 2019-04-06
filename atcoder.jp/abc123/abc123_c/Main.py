n=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

def f(a):
    if n%a==0:
        return n//a
    else:
        return n//a+1
l=[]
for i in [a,b,c,d,e]:
    l.append(f(i))

print(max(l)+4)

