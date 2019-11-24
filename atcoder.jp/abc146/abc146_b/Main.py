n=int(input())
s=input()

ans=""
for i in s:
    m=ord(i)+n
    if m>90:
        m-=90
        m+=64
    ans+=chr(m)
print(ans)




