n=int(input())
a=[int(j) for j in input().split()]

m=0

for i in range(n):
    o=0
    while o<1:
        if a[i]%2==0:
            m+=1
            a[i]=a[i]/2
        else:
            o=1
            
print(m)