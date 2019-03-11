n,m = map(int,input().split())
ab=[]
for i in range(n):
    ab.append([int(j) for j in input().split()])
ab.sort()
cnt = 0
ans = 0
for i in ab:
    cnt += int(i[1])
    ans += int(i[0])*int(i[1])
    if cnt >= m:
        ans -= int(i[0])*(cnt-m)
        print(ans)
        break