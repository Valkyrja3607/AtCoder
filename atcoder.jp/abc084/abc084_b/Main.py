a,b=map(int,input().split())
s=input()
if s[a]=="-":
    if "-" not in s[:a] and "-" not in s[a+1:]:
        print("Yes")
        exit()
print("No")