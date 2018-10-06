n,T=map(int,input().split())

c=[]
t=[]

for i in range(n):
    a,b=map(int,input().split())
    c.append(a)
    t.append(b)

ans=1000000   
for i in range(n):
    if t[i]<=T:
        ans=min(ans,c[i])
        
if ans==1000000:
    print("TLE")
else:
    print(ans)