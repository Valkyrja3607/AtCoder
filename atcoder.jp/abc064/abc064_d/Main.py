n=int(input())
s=input()
c1=0
c2=0
p=10**100
q=10**100
for i in s:
    if i=="(":
        c1+=1
    else:
        c1-=1
    p=min(p,c1)
if p<0:
    s="("*abs(p)+s

for i in range(1,len(s)+1):
    if s[-i]==")":
        c2+=1
    else:
        c2-=1
    q=min(q,c2)
if q<0:
    s=s+")"*abs(q)
print(s)