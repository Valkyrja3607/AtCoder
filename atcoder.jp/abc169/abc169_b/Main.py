n = int(input())
a = [int(j) for j in input().split()]
a.sort()
ans = 1
for i in a:
    ans *= i
    if ans > 10 ** 18:
        print(-1)
        exit()
print(ans)