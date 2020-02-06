from subprocess import*
call(('pypy3','-c',"""

n=int(input())
a=[int(i) for i in input().split()]
a.sort()

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

l=make_divisors(a[0])
l2=make_divisors(a[1])
le=len(l)
le2=len(l2)         
an=[0]*le
an2=[0]*le2
for i in range(n):
    for j in range(le):
        if a[i]%l[j]==0:
            an[j]+=1
    for j in range(le2):
        if a[i]%l2[j]==0:
            an2[j]+=1
ans=1
ans2=1
for i in range(le):
    if an[i]>=n-1:
        ans=max(ans,l[i])
for i in range(le2):
    if an2[i]>=n-1:
        ans2=max(ans2,l2[i])

print(max(ans,ans2))


"""))