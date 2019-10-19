n=int(input())
s=input()
from itertools import*
g=[len(list(v))for k,v in groupby(s)]
print(len(g))
