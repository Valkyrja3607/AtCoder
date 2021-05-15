n=int(input())
s=[]
for i in range(n):
    name,t=input().split()
    s.append([int(t),name])
s.sort()
print(s[-2][1])