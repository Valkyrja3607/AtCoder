n,m=map(int,input().split())
mod=10**9+7
a=[]
for i in range(m):
    a.append(int(input()))
aa=set(a)
l=[0 for i in range(n+1)]
l[0]=1

for i in range(n):
    if i+1 not in aa:
        l[i+1]+=l[i]
        l[i+1]=l[i+1]%mod
    if i+2 not in aa and i+2<n+1:
        l[i+2]+=l[i]
        l[i+2]=l[i+2]%mod

print(l[n])