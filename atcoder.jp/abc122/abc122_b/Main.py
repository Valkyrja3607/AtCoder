s=input()

ans=0
p=0
for i in s:
    if i=="A" or i=="T" or i=="G" or i=="C":
        p+=1
    else:
        p=0
    ans=max(ans,p)

print(ans)



