n=int(input())
l=[]
s=0
for i in range(n):
    a,b=map(int,input().split())
    l.append([a+b+a,a+b,a])
    s+=a
l.sort()
ans=0
tmp=0
for i,j,k in l[::-1]:
    ans+=1
    tmp+=j
    s-=k
    if tmp>s:
        break
print(ans)