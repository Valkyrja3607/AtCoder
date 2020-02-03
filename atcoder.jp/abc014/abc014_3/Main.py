n=int(input())
table=[0]*(10**6+2)
for i in range(n):
    a,b=map(int,input().split())
    table[a]+=1
    table[b+1]-=1
from itertools import accumulate
print(max(list(accumulate(table))))