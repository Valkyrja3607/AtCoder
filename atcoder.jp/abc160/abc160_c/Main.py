k,n=[int(j) for j in input().split()]
a=[int(j) for j in input().split()]
l=[]
for i,j in zip(a,a[1:]):
    l.append(j-i)
l.append(k-a[-1]+a[0])
print(k-max(l))