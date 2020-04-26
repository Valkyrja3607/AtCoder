n,m=map(int,input().split())
a=[int(j) for j in input().split()]
a.sort(reverse=True)
s=sum(a)/(4*m)
for i in a[:m]:
    if i<s:
        print("No")
        exit()
print("Yes")