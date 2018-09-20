n=int(input())
m=0
a=0
r=0
c=0
h=0


for i in range(n):
    s=input()
    if s[0]=="M":
        m+=1
    if s[0]=="A":
        a+=1
    if s[0]=="R":
        r+=1
    if s[0]=="C":
        c+=1
    if s[0]=="H":
        h+=1

l=[m,a,r,c,h]
ans=0

for i in range(2,5):
    for j in range(1,i):
        for k in range(j):
            ans+=l[i]*l[j]*l[k]
            
print(ans)

