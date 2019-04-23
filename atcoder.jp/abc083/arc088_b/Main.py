s=input()
n=len(s)
ans=0

la=[0]
lb=[0]

for i in s:
    if i=="0":
        la.append(la[-1]+1)
        lb.append(lb[-1])
    else:
        lb.append(lb[-1]+1)
        la.append(la[-1])

if n%2==0:
    for i in range(n//2+1):
        if la[n//2+i]-la[n//2-i]==0 or lb[n//2+i]-lb[n//2-i]==0:
            ans=n//2+i
else:
    for i in range(n//2+1):
        if la[n//2+i+1]-la[n//2-i]==0 or lb[n//2+i+1]-lb[n//2-i]==0:
            ans=n//2+i+1

print(ans)