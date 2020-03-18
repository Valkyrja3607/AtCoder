n=int(input())
b=[int(input()) for i in range(n)]
a=[0]
for i in range(n-1):
    a.append(a[-1]^b[i])

if a[-1]!=b[-1]:
    print(-1)
else:
    print('\n'.join(map(str,a)))