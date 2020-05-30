n,*a=map(int,open(0).read().split())
ans=0
s=sum(a)
p=1
b=True
for j in a:
    if p<j:
        print(-1)
        exit()
    ans+=p
    p-=j
    s-=j
    if p<s and b:
        if p*2<s:p*=2
        else:p=s
    if p==s:b=False
print(ans)