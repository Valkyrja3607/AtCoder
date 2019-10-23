o=input()
e=input()
ans=""
for i in range(len(e)):
    ans+=o[i]+e[i]
if len(e)!=len(o):
    print(ans+o[-1])
else:
    print(ans)