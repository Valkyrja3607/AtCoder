n,k,q=[int(j) for j in input().split()]
l=[0]*n
for i in range(q):
    a=int(input())
    l[a-1]+=1
s=sum(l)
ans=0
for i in range(n):
    if k-s+l[i]>0:
        print("Yes")
    else:
        print("No")
