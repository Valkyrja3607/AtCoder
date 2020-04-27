N, M = map(int, input().split())
X = [[] for _ in range(N)]
for _ in range(M):
    u, v, d = map(int, input().split())
    X[u-1].append((v-1, d))
    X[v-1].append((u-1, d))
input()    
T = int(input())
t = 0
x = 0
while t < T:
    if t < 5000:
        print(-1)
        t += 1
        continue
    
    y, d = max([(y, d) for y, d in X[x]])
    for i in range(d):
        print(y+1)
        t += 1
        if t >= T:
            break
    x = y