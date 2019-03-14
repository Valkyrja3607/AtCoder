n=int(input())

def eratosthenes(n):
    table = [0] * (n + 1)
    prime_list = []
    
    for i in range(2, n + 1):
        if table[i] == 0:
            prime_list.append(i)
            for j in range(i + i, n + 1, i):
                table[j] = 1
                
    return prime_list
p=eratosthenes(55555)
ans=[]

c=0
for i in p:
    if i%5==1:
        print(i,end=" ")
        c+=1
    if c==n:
        break

print("")