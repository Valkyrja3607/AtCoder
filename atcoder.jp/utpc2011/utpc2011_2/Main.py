s=input()
n=len(s)
ans=0
for i in range(n//2):
    if s[i]=="(":
        if s[-1-i]==")":
            continue
        else:
            ans+=1
    elif s[i]==")":
        if s[-1-i]=="(":
            continue
        else:
            ans+=1
    elif s[i]==s[-1-i]:
        continue
    else:
        ans+=1
if n%2==1:
    if s[n//2]=="(" or s[n//2]==")":
        ans+=1
print(ans)