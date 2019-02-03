n=int(input())
l=[int(i) for i in input().split()]

s=sum(l)
p=0
for i in l:
    if s-2*i<=0:
        p=1

if p==0:
    print("Yes")
else:
    print("No")