h,w=map(int,input().split())
s=[input()for i in range(h)]
from functools import lru_cache
@lru_cache(maxsize=10000)
def f(i,j):
    res=False
    for x,y in [(1,0),(0,1),(1,1)]:
        if i+x<h and j+y<w:
            if s[i+x][j+y]==".":
                res=res or (not f(i+x,j+y))
    return res
if f(0,0):print("First")
else:print("Second")    