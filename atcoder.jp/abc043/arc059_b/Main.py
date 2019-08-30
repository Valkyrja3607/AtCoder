s=input()
n=len(s)
if n==2:
    if s[0]==s[1]:
        print(1,2)
        exit()
for i in range(n-2):
    a,b,c=s[i],s[i+1],s[i+2]
    if a==b or a==c or b==c:
        print(i+1,i+3)
        exit()
print(-1,-1)
