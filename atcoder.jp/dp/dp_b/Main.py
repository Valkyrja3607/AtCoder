n,k=map(int,input().split())
h=[int(i) for i in input().split()]

l=[0]+[100000000000000000000000000000 for i in range(n-1)]

for i in range(n-1):
    if i<n-k:
        for j in range(k):
            l[i+j+1]=min(l[i+j+1],abs(h[i]-h[i+j+1])+l[i])
    else:
        for j in range(n-i-1):
            l[i+j+1]=min(l[i+j+1],abs(h[i]-h[i+j+1])+l[i])

print(l[-1])
        


