s=input()
n=len(s)
ans=n*(n-1)
for i in range(n):
    if s[i]=="U":
        ans+=i
    else:
        ans+=n-i-1
print(ans)