a,b,c=map(int,input().split())

x=max(a,b,c)
z=min(a,b,c)
y=a+b+c-x-z

ans=x-y
y=x
z+=ans

if (x-z)%2==0:
    ans+=(x-z)/2
else:
    x+=1
    ans+=1
    ans+=(x-z)/2

print(int(ans))