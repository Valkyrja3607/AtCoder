n,l=map(int,input().split())
ll=[]
p=10*100
for i in range(n):
    ll.append(l+i)
    if abs(p)>abs(l+i):
        p=l+i
print(sum(ll)-p)
