n=int(input())
a=[int(input()) for i in range(n)]

tmp=a[0]

for i in range(1,n):
    if a[i]==tmp:
        print("stay")
    elif a[i]>tmp:
        print("up",a[i]-tmp)
        tmp=a[i]
    else:
        print("down",tmp-a[i])
        tmp=a[i]