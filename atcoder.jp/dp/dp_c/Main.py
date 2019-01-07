n=int(input())
l=[]
for i in range(n):
    a=[int(j) for j in input().split()]
    if i==0:
        l.append(a)
    else:
        li=[]
        li.append(a[0]+max(l[-1][1],l[-1][2]))
        li.append(a[1]+max(l[-1][0],l[-1][2]))
        li.append(a[2]+max(l[-1][0],l[-1][1]))
        l.append(li)

print(max(l[-1]))
