n=int(input())
s=input()
t=input()
ans=[2*n]

for i in range(n):
    if s[n-i-1:n]==t[0:i+1]:
        ans.append(2*n-i-1)

print(min(ans))
