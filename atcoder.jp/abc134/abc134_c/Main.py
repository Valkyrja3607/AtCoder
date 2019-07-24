n=int(input())
a=[]
l=[]
for i in range(n):
    p=int(input())
    a.append(p)
    l.append(p)
a.sort()
a=a[::-1]
if a[0]==a[1]:
    for i in range(n):
        print(a[0])
else:
    for i in range(n):
        if l[i]==a[0]:
            print(a[1])
        else:
            print(a[0])



