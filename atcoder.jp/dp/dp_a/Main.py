n=int(input())
h=[int(i) for i in input().split()]

l=[0]+[100000000000000000000000000000 for i in range(n-1)]

for i in range(n-1):
    if i!=n-2:
        l[i+1]=min(l[i+1],abs(h[i]-h[i+1])+l[i])
        l[i+2]=min(l[i+2],abs(h[i]-h[i+2])+l[i])
    else:
        l[i+1]=min(l[i+1],abs(h[i]-h[i+1])+l[i])

print(l[-1])
        


