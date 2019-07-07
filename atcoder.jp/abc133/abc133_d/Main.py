n=int(input())
a=[int(i) for i in input().split()]
ans=[]
l=[a[0]*2]
for i in range(1,n):
    l.append(a[i]*2-l[-1])

x=a[-1]-(l[-2]//2)

print(x,end=" ")
for i in range(1,n):
    if i%2==0:
        print(l[i-1]+x,end=" ")
    else:
        print(l[i-1]-x,end=" ")
print("")