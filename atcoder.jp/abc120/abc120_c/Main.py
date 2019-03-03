s=input()
ls=len(s)
sz=0
so=0

for i in range(ls):
    if s[i]=="0":
        sz+=1
    else:
        so+=1

print(min(so,sz)*2)