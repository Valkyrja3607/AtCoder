n=int(input())
l=[int(input())-1 for i in range(n)]
ans=0
j=0
for i in range(n):
    j=l[j]
    ans+=1
    if j==1:
        print(ans)
        exit()
print(-1)