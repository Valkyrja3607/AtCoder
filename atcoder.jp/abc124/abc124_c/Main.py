s=input()
l=len(s)
p=""
ans=0
for i in range(l):
    if i%2==0:
        if s[i]=="1":
            ans+=1
    else:
        if s[i]=="0":
            ans+=1
print(min(ans,l-ans))