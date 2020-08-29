s=input()
t=input()
n=len(s)
m=len(t)
ans=100000000
for i in range(n-m+1):
    tmp=0
    for x,y in zip(t,s[i:i+m]):
        if x!=y:
            tmp+=1
    ans=min(ans,tmp)
print(ans)