n,c,k=map(int,input().split())
t=[]
for i in range(n):
    t.append(int(input()))
t.sort()
ans=0
p=0
q=0
for i in range(n):
    if p==0:
        p=t[i]
        ans+=1
        q=i
    elif t[i]>p+k or i>=q+c:
        p=t[i]
        ans+=1
        q=i
print(ans)



