import collections
n=int(input())
a=[int(i) for i in input().split()]


ans=0

l=collections.Counter(a)

for i,j in l.most_common():
    if int(i)<j:
        ans+=j-int(i)
    elif int(i)>j:
        ans+=j
        
print(ans)