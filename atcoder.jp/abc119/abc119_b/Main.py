n=int(input())
xu=[]
ans=0
for i in range(n):
    a=[j for j in input().split()]
    if a[1]=="JPY":
        ans+=int(a[0])
    else:
        ans+=float(a[0])*380000

print(ans)