h,w=map(int,input().split())
for i in range(1,1+h):
    s=input().split()
    for j in range(w):
        if s[j]=="snuke":
            print(chr(65+j)+str(i))
            exit()