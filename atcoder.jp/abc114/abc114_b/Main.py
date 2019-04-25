s=input()
l=len(s)
ans=10000000
for i in range(l-2):
    ans=min(ans,abs(753-int(s[i:i+3])))

print(ans)