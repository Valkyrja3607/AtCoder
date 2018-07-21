a=[int(i) for i in input().split()]

a.sort()
b=[a[2]-a[1],a[1]-a[0],a[2]-a[0]]


print(sum(b)-max(b))