x,y=map(int,input().split())

ans=10**100
if y-x>=0:
    ans=min(ans,y-x)
if 1+y+x>0:
    ans=min(ans,1+y+x)
if -y-x+1>0:
    ans=min(ans,-y-x+1)
if -y+x>=0:
    ans=min(ans,-y+x+2)
print(ans)