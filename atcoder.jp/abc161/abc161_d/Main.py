k=int(input())
from collections import deque
q=deque(list(range(1,10)))
for i in range(k):
    p=q.popleft()
    if i==k-1:
        print(p)
        exit()
    a=p%10
    if 0<a<9:
        q.append(p*10+a-1)
        q.append(p*10+a)
        q.append(p*10+a+1)
    elif a==0:
        q.append(p*10)
        q.append(p*10+1)
    else:
        q.append(p*10+a-1)
        q.append(p*10+a)