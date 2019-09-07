n=int(input())
s=[j for j in input().split()]
for i in s:
    if i=="Y":
        print("Four")
        exit()
print("Three")