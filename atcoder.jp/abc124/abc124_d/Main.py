n,k=map(int,input().split())
s=input()


l=[]
p="1"
q=0
for i in s:
    if i==p:
        q+=1
    else:
        l.append(q)
        q=1
        if p=="1":
            p="0"
        else:
            p="1"
l.append(q)

r=[0]
def ruiseki(a):
    for i in range(len(a)):
        r.append(r[i]+a[i])
ruiseki(l)
ans=0

if len(r)-(2*k+2)+1<=0:
    print(r[-1])
    import sys
    sys.exit()
    
for i in range(len(r)-(2*k+2)+1):
    if (i+2*k+1)%2==1:
        ans=max(ans,r[i+2*k+1]-r[i])
ans=max(ans,r[-1]-r[len(r)-(2*k+2)+1])
print(ans)