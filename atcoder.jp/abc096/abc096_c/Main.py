import sys

h,w=map(int,input().split())

s=[["" for i in range(w)] for j in range(h)]

for i in range(h):
    a=input()
    for j in range(w):
        s[i][j]=a[j]
        
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            if i != 0:
                if s[i-1][j] == "#":
                    continue
            if i != h-1:
                if s[i+1][j] == "#":
                    continue
            if j != 0:
                if s[i][j-1] == "#":
                    continue
            if j != w-1:
                if s[i][j+1] == "#":
                    continue
            print("No")
            sys.exit()
print("Yes")