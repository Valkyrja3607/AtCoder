n=int(input())
ans=10**100
for t in range(n+1):
    p=t
    q=n-p
    c=0
    while p>0:
        c+=p%6
        p=p//6
    while q>0:
        c+=q%9
        q=q//9
    ans=min(ans,c)
print(ans)






