s=input()
ls=len(s)
k=1
ans=0

for i in range(ls):
    if s[i]=="W":
        ans+=i-k+1
        k+=1

print(ans)
    