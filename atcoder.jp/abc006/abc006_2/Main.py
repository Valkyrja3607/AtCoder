n=int(input())-1
l=[0,0,1]
mod=10**4+7
if n<=2:
    print(l[n])
    exit()
for i in range(n-2):
    ans=sum(l)%mod
    l=l[1:]+[ans]
print(ans)