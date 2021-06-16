n=int(input())
s=set()
for i in range(1,1+n):
    m=input()
    if m not in s:
        print(i)
    s.add(m)