n=int(input())
x=[int(i) for i in input().split()]
y=[]
for i in x:
    y.append(i)
x.sort()

c=int(n/2)
a=x[c]
b=x[c-1]

for i in y:
    if i<=b:
        print(a)
    else:
        print(b)

