l=input()
n=len(l)
s=list(l)
i=0
ans=0
p=0
while i<n-2:
    if s[i]=="A":
        p+=1
    else:
        p=0
    if s[i]=="A" and s[i+1]=="B" and s[i+2]=="C":
        ans+=p
        i+=2
        s[i]="A"
        p-=1
    else:
        i+=1
print(ans)
        