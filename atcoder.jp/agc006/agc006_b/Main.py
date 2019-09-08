n,x=map(int,input().split())
m=2*n-1
if x==1 or x==m:
    print("No")
    exit()
if n==2:
    print("Yes")
    for i in [1,2,3]:
        print(i)
    exit()
ll=list(range(1,2*n))
if x!=2:
    l=[x-1,x,x+1,x-2]
    ll.remove(x-1)
    ll.remove(x)
    ll.remove(x+1)
    ll.remove(x-2)
else:
    l=[x+1,x,x-1,x+2]
    ll.remove(x-1)
    ll.remove(x)
    ll.remove(x+1)
    ll.remove(x+2)

ans=[]
for i in range(len(ll)):
    if i==n-2:
        ans+=l
    ans.append(ll[i])
if len(ll)==n-2:
    ans+=l
print("Yes")
for i in ans:
    print(i)

