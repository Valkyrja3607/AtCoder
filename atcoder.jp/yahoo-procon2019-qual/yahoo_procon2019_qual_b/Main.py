l=[[]for i in range(5)]
for i in range(3):
    a=[int(j) for j in input().split()]
    l[a[0]].append(a[1])
    l[a[1]].append(a[0])
p=0
for i in range(5):
    if len(l[i])>=3:
        p=1

if p==1:
    print("NO")
else:
    print("YES")