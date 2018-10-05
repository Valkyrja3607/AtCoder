import sys
n,m=map(int,input().split())

for j in range(2):
    for i in range(n-j+1):
        if 2*i+3*j+4*(n-i-j)==m:
            print(i,j,n-i-j)
            sys.exit()

print(-1,-1,-1)