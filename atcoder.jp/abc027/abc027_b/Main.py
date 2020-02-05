n=int(input())
a=[int(j) for j in input().split()]
if sum(a)%n==0:
    m=sum(a)//n
else:
    print(-1)
    exit()
c=0
j=1
ans=0
for i in a:
    c+=i
    if c==m*j:
        ans+=j-1
        c=0
        j=1
    else:
        j+=1
print(ans)