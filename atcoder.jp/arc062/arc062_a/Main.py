n=int(input())
ta=[]
t=0
a=0
ans=[[1,1]]
for i in range(n):
    p=[int(j) for j in input().split()]
    i=max(ans[-1][0]//p[0],ans[-1][1]//p[1])
    while True:
        if p[0]*i>=ans[-1][0] and p[1]*i>=ans[-1][1]:
            ans.append([p[0]*i,p[1]*i])
            break
        i+=1

print(sum(ans[-1]))