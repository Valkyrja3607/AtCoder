n=int(input())
l=list(map(int,input().split()))
t=0
ans=0
for i in l:
    if i<t:
        ans+=t-i
    else:
        t=i
print(ans)