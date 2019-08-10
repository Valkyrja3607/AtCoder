n=int(input())
s=[]
for i in range(n):
    p=input()
    l=list(p)
    l.sort()
    p="".join(l)
    s.append(p)
s.sort()
q=""
ans=0
qq=1
for i in range(n):
    if i!=n-1:
        if q==s[i]:
            qq+=1
        else:
            q=s[i]
            ans+=qq*(qq-1)//2
            qq=1
    else:
        if q==s[i]:
            qq+=1
        ans+=qq*(qq-1)//2
print(ans)