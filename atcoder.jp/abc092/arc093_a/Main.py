n=int(input())
a=[0]
for i in input().split():
    a.append(int(i))
a.append(0)

s=0
for i in range(n+1):
    s+=abs(a[i]-a[i+1])


for i in range(n):
    print(s+abs(a[i]-a[i+2])-abs(a[i]-a[i+1])-abs(a[i+1]-a[i+2]))