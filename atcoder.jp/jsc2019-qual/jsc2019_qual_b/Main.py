n,k=[int(j) for j in input().split()]
a=[int(j) for j in input().split()]

l=[]
l1=[]
for i in range(n):
    p=0
    for j in a:
        if j>a[i]:
            p+=1
    l.append(p)

for i in range(n):
    p=0
    for j in range(i):
        if a[j]>a[i]:
            p+=1
    l1.append(p)

ans=0
mod=10**9+7
for i in range(n):
    ans+=k*(2*l1[i]+(k-1)*(l[i]))//2
    ans=ans%mod
print(ans)




