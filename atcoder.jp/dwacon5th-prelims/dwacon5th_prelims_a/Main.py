n=int(input())
a=[int(i) for i in input().split()]

h=sum(a)/n
ans=0
an=0
k=abs(h-a[0])

for i in range(n):
    if k>abs(h-a[i]):
        k=abs(h-a[i])
        ans=i
        
print(ans)
        