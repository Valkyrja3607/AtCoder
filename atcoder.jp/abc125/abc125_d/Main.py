n=int(input())
a=[int(i) for i in input().split()]
ans=0
m=100000000000
p=0
for i in a:
    if i<0:
        p+=1
    m=min(m,abs(i))
    ans+=abs(i)

if p%2==0:
    print(ans)
else:
    print(ans-m*2)