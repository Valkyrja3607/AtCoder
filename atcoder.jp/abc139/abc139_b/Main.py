a,b=[int(j) for j in input().split()]
ans=0
p=1
while p<b:
    p+=a-1
    ans+=1
print(ans)