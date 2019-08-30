n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append([s[::-1],s])
l.sort()
for i,j in l:
    print(j)