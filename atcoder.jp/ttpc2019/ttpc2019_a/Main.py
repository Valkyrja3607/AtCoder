a,b,t=map(int,input().split())
ans=b
while ans<t:
    ans+=b-a
print(ans)