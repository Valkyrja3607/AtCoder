s=input()
t=input()

ls=len(s)
lt=len(t)

def f(a,b):
    r=""
    for i in range(lt):
        if a[i]==b[i] or a[i]=="?":
            r+=b[i]
        else:
            return False
    return True
        
ans=[]

for i in range(ls-lt+1):
    c=""
    if f(s[i:i+lt],t):
        c+=s[0:i]
        c+=t
        c+=s[i+lt:ls]
        c=c.replace("?","a")
        ans.append(c)

if ans==[]:
    print("UNRESTORABLE")
else:
    print(min(ans))
