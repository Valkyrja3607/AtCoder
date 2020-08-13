x = int(input())
t = 100
ans = 0
while t < x:
    t += t // 100
    ans += 1
print(ans)