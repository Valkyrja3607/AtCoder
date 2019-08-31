n=int(input())
b=[int(j) for j in input().split()]
ans=[]
while b:
    tmp=10**18
    for i in range(len(b))[::-1]:
        if b[i]==i+1:
            tmp=i
            break
    if tmp==10**18:
        print(-1)
        exit()
    else:
        ans.append(b[tmp])
        del b[tmp]

for i in range(n)[::-1]:
    print(ans[i])