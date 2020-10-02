n=int(input())
a=[0]*30
for i in input().split():
    a[int(i)]+=1
print(*a)   