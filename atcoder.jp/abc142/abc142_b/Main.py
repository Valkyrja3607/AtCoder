n,k=[int(j) for j in input().split()]
h=[int(j) for j in input().split()]
ans=0
for i in h:
    if i>=k:
        ans+=1
print(ans)