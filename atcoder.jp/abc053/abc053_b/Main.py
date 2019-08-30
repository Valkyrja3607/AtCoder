s=input()
n=len(s)
f=0
l=0
for i in range(n):
    if s[i]=="A":
        f=i
        break
for i in range(n)[::-1]:
    if s[i]=="Z":
        l=i
        break
print(l-f+1)