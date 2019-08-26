n,k=map(int,input().split())
l=[int(i) for i in input().split()]

l.sort()
l.reverse()
print(sum(l[:k]))


