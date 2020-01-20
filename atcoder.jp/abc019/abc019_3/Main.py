n=int(input())
a=[int(j) for j in input().split()]
s=set()

for i in a:
    while i%2==0:
        i=i//2
    s.add(i)
print(len(s))