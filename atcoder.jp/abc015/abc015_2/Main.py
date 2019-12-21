n=int(input())
a=[int(j) for j in input().split()]
print(-(-sum(a)//(n-a.count(0))))