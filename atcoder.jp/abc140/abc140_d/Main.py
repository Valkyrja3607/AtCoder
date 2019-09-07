n,k=[int(j) for j in input().split()]
s=input()
l=[1]
for i in range(1,n):
    if s[i]==s[i-1]:
        l[-1]+=1
    else:
        l.append(1)
if len(l)//2<=k:
    print(n-1)
    exit()
ans=sum(l)-len(l)
ans+=2*k
print(ans)
