n,m=map(int,input().split())
s=[input()for i in range(n)]
l=[0,0]
for i in range(n):
    l[s[i].count("1")%2]+=1
print(l[0]*l[1])