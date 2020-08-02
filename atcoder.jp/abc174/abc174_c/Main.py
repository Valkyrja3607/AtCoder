k=int(input())
if k%7==0:
    k//=7
tmp=0
for i in range(10**6+1):
    tmp=(tmp+pow(10,i,k))%k
    if tmp==0:
        print(i+1)
        exit()
print(-1)