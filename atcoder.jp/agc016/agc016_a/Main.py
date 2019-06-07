s=input()
n=len(s)
ans=100000
l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
s+="a"
for i in l:
    s=s[0:n]+i
    c=0
    p=0
    for j in range(n+1):
        if s[j]==i:
            p=max(c,p)
            c=0
        else:
            c+=1
    ans=min(ans,p)
print(ans)
    