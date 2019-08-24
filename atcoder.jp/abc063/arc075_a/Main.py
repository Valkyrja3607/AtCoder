n=int(input())
s=[]
l=[]
for i in range(n):
    p=int(input())
    s.append(p)
    if p%10!=0:
        l.append(p)
ans=sum(s)
if ans%10==0:
    if l==[]:
        print(0)
    else:
        print(ans-min(l))
else:
    print(ans)



