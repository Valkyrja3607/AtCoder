n=int(input())
s=input()

def f(l,r):
    li=[]
    re=0
    for i in range(len(l)):
        if l[i] in r and l[i] not in li:
            re+=1
            li.append(l[i])
    return re
            
ans=0

for i in range(1,n):
    sl=s[:i]
    sr=s[i:]
    ans=max(ans,f(sl,sr))

print(ans)

