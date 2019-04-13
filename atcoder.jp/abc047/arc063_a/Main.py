s=input()
if s[0]=="W":
    j="B"
else:
    j="W"
ans=-1   
for i in s:
    if i!=j:
        ans+=1
        j=i

print(ans)
