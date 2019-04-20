n=int(input())
s=input()
la=[0]
lb=[0]
for i in s:
    if i==".":
        la.append(la[-1]+1)
        lb.append(lb[-1])
    if i=="#":
        la.append(la[-1])
        lb.append(lb[-1]+1)

ans=1000000000000
for i in range(n+1):
    ans=min(ans,lb[i]-lb[0]+la[-1]-la[i])
print(ans)