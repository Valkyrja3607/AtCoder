l=input().split("+")
ans=0
for i in l:
    if "0" not in i:
        ans+=1
print(ans)