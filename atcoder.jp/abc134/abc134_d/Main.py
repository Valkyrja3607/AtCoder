n=int(input())
a=[0]+[int(i) for i in input().split()]
m=0
ans=[]
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors
for i in range(n,0,-1):
    if a[i]%2==1:
        m+=1
        ans.append(i)
        l=make_divisors(i)
        for j in l:
            a[j]+=1
print(m)
if ans!=[]:
    for i in range(m):
        if i!=m-1:
            print(ans[i],end=" ")
        else:
            print(ans[i])
