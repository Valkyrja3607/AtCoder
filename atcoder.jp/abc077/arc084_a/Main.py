n=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
c=[int(i) for i in input().split()]
a.sort()
b.sort()
c.sort()

ans=0
p=0
q=0

for i in b:
    while p<n and a[p]<i:
        p+=1
    while q<n and c[q]<=i:
        q+=1
    ans+=p*(n-q)

print(ans)