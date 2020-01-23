n=int(input())
s=[input() for i in range(n)]
import collections
c=collections.Counter(s)
print(c.most_common()[0][0])