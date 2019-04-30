n,t=map(int,input().split())
a=[int(i) for i in input().split()]
p=a[0]
l=[]
for i in range(n):
    p=min(p,a[i])
    if a[i]-p>0:
        l.append(a[i]-p)

print(l.count(max(l)))