s=input()
n=len(s)
m=n//2
ans=25*n
c=0
for i in range(m):
    if s[i]==s[-i-1]:
        c+=1
if c==m-1:
    ans-=2
if c==m and n%2==1:
    ans-=25

print(ans)