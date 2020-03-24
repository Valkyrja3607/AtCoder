a,b=map(int,input().split())

for i in range(10001):
    if i//10==b and int(i*0.08)==a:
        print(i)
        exit()
print(-1)