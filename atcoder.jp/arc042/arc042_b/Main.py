import sys
input=sys.stdin.readline
x,y=[int(j) for j in input().split()]
n=int(input())
xy=[[int(j) for j in input().split()] for i in range(n)]
ans=10**18
for i in range(n):
    a,b=xy[i-1]
    c,d=xy[i]
    tmp=abs((b-d)*x+(c-a)*y+(a*d-b*c))/((b-d)**2+(c-a)**2)**0.5
    if ans>tmp:
        ans=tmp
print(ans)