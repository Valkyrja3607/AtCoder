n=int(input())
a=list(map(int,input().split()))
q=int(input())
a.sort()
import bisect
for i in range(q):
    b=int(input())
    j=bisect.bisect_left(a,b)
    try:
        print(min(abs(b-a[j]),abs(b-a[j-1])))
    except:
        print(abs(b-a[j-1]))