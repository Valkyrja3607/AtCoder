n,r=[int(j) for j in input().split()]
s=input()
ans=0
while n>0:
    n-=1
    if s[n]==".":
        n-=r-1
        ans=max(ans,n)+1
print(ans)