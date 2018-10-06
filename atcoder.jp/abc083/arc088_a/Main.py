x,y=map(int,input().split())

ans=1

while x<=y:
    x*=2
    if x<=y:
        ans+=1

print(ans)