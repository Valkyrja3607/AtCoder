s=input()
t=input()
n=len(s)
for i in range(n):
    if s[i]==t[i]:
        continue
    elif s[i]=="@":
        if t[i] in "@atcoder":
            continue
    elif t[i]=="@":
        if s[i] in "@atcoder":
            continue
    print("You will lose")
    exit()
print("You can win")