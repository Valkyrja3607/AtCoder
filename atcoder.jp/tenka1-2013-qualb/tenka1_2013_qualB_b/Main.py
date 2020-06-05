q,L=map(int,input().split())
from collections import deque
s=deque([])
c=0
for _ in range(q):
    l=input().split()
    if l[0]=="Push":
        n,m=map(int,l[1:])
        s.append([n,m])
        c+=n
        if c>L:
            print("FULL")
            exit()
    if l[0]=="Pop":
        n=int(l[1])
        c-=n
        while n>0:
            if s:
                i,j=s.pop()
                n-=i
            else:
                print("EMPTY")
                exit()
        if n<0:
            s.append([-n,j])
    if l[0]=="Top":
        if s:
            print(s[-1][1])
        else:
            print("EMPTY")
            exit()
    if l[0]=="Size":
        print(c)
print("SAFE")