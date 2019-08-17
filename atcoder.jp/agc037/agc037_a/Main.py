s=input()
n=len(s)
ans=0
p=s[0]
q=""
i=0
while i<n-1:
    if p==s[i+1]:
        ans+=1
        q=p
        p=s[i+1:i+3]
        i+=1
    else:
        ans+=1
        q=p
        p=s[i+1]
    i+=1
if i==n-1:
    if len(p)==1:
        if q!=p:
            ans+=1
    else:
        ans+=1

print(ans)
