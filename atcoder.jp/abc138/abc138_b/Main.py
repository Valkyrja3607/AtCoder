n=int(input())
a=[int(i) for i in input().split()]
p=0
for i in range(n):
    p+=1/a[i]
print(1/p)