n=int(input())
v=[int(i) for i in input().split()]
v.sort()
p=v[0]
for i in range(1,n):
    p=(p+v[i])/2
print(p)