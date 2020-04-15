n,x,y=[int(j) for j in input().split()]
ans=[0]*n
for i in range(1,1+n):
    for j in range(i+1,1+n):
        t=min(j-i,abs(x-i)+abs(y-j)+1)
        ans[t]+=1
print('\n'.join(map(str,ans[1:])))