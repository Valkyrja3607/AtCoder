a,b,c=map(int,input().split())
q=set()
ans=0
while True:
    if (a,b,c) in q:
        print(-1)
        exit()
    q.add((a,b,c))
    if a%2==0 and b%2==0 and c%2==0:
        ans+=1
        a,b,c=(b+c)//2,(a+c)//2,(b+a)//2
    else:
        break
print(ans)
    
    
