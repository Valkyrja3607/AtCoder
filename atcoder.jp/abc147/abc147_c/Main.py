n=int(input())
xy=[[] for i in range(n)]
for i in range(n):
    a=int(input())
    for j in range(a):
        p,q=[int(k) for k in input().split()]
        xy[i].append([p-1,q])
ans=0
for i in range(2**n):
    s=bin(i)[2:].rjust(n,'0')
    r,t=0,0
    for j in range(n):
        if s[j]=="1":
            p,q=0,0
            for x,y in xy[j]:
                p+=1
                if s[x]!=str(y):
                    break
                q+=1
            if p!=q:
                break
            else:
                r+=1
        else:
            r+=1
        t+=1
    if r==n:
        ans=max(ans,s.count("1"))
        
            
print(ans)
