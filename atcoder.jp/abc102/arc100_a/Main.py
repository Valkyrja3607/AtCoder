n=int(input())
a=[int(i) for i in input().split()]

for i in range(n):
    a[i]-=i+1

a.sort()
if n % 2 == 0:
    print(sum(a[int(n / 2):]) - sum(a[:int(n / 2)]))
else:
    print(sum(a[int((n + 1) / 2):]) - sum(a[:int((n - 1) / 2)]))
