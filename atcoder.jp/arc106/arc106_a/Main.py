n=int(input())
for i in range(1,61):
    for j in range(1,61):
        if pow(3,i)+pow(5,j)==n:
            print(i,j)
            exit()
print(-1)