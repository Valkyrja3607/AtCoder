n=int(input())
l="zabcdefghijklmnopqrstuvwxy"
ans=""
while n>0:
    ans=l[n%26]+ans
    if n%26==0:n-=1
    n//=26
print(ans)