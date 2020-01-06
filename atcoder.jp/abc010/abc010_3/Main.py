import sys
input=sys.stdin.readline
xa,ya,xb,yb,t,v=map(int,input().split())
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    if (((x-xa)**2+(y-ya)**2)**0.5)+(((x-xb)**2+(y-yb)**2)**0.5)<=t*v:
        print("YES")
        exit()
print("NO")