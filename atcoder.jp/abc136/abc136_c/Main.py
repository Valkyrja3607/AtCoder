n=int(input())
h=[int(i) for i in input().split()]
p=-10**101
for i in range(n):
    if p>h[i]:
        if p!=h[i]+1:
            print("No")
            exit()
        else:
            p=h[i]+1
    else:
        p=h[i]
print("Yes")