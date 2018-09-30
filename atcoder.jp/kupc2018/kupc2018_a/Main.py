n=int(input())

s=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
ans=[]
for i in range(n):
    ans.append(s[i]*a[i])
    
print(max(ans))