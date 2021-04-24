n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=set(range(a[0],b[0]+1))
for i,j in zip(a,b):
    ans&=set(range(i,j+1))
print(len(ans))



