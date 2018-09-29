n=input()
ans=""
an=""

for i in n:
    ans+=n[0]
    
if int(ans)>=int(n):
    print(ans)
else:
    for i in n:
        an+=str(int(n[0])+1)
    print(an)