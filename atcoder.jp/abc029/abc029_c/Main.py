n=int(input())
ans=[]

def base(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out

for i in range(3**n):
    ans.append(base(i,3).rjust(n,'0').replace("0","a").replace("1","b").replace("2","c"))
ans.sort()
for i in ans:
    print(i)
