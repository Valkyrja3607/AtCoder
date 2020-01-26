n,k=[int(j) for j in input().split()]
h=[int(j) for j in input().split()]
h.sort()
print(sum(h[:max(0,n-k)]))