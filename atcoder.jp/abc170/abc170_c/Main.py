x,n=map(int,input().split())
p=set(map(int,input().split()))
l=set(range(-100,201))-p
ans=0
tmp=1000
for i in l:
    if tmp>abs(x-i):
        ans=i
        tmp=abs(x-i)
print(ans)