n=int(input())
a=[int(j) for j in input().split()]
l=[]
for i in range(n):
    l.append([a[i],i])
l.sort()
for i,j in reversed(l):
    print(j+1)




