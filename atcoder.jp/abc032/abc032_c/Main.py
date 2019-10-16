n,k=map(int,input().split())
s=[int(input()) for i in range(n)]
i=0
ans=0
tmp=1
l=0
if 0 in set(s):
    print(n)
    exit()
if k==0:
    print(0)
    exit()
for j in range(n):
    tmp*=s[j]
    ans+=1
    if tmp>k:
        while tmp>k:
            tmp=tmp//s[i]
            i+=1
            ans-=1
    l=max(l,ans)
print(l)
        
    


