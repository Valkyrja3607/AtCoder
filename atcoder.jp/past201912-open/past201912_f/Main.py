s=input()
tmp=""
l=[]
for i in s:
    if 65<=ord(i)<=90:
        if tmp=="":
            tmp+=chr(ord(i)+32)
        else:
            tmp+=chr(ord(i)+32)
            l.append(tmp)
            tmp=""
    else:
        tmp+=i

l.sort()
ans=[]
for s in l:
    tmp=chr(ord(s[0])-32)+s[1:-1]+chr(ord(s[-1])-32)
    ans.append(tmp)
print("".join(ans))

