n=int(input())
a=[int(i) for i in input().split()]

t=0
ans=0
for i in a:
    if i==t:
        ans+=1
        t=0
    else:
        t=i

print(ans)
