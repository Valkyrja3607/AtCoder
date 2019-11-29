n=int(input())
s=int(len(str(n)))*9
ans=[]
def wa(n):
    n=list(str(n))
    return sum(map(int,n))

for i in range(max(n-s,0),n+1):
    if i+wa(i)==n:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i)