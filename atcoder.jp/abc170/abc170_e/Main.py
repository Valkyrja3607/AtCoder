import heapq
def main():
    n,q=map(int,input().split())
    ans=[]
    infants=[[]]
    y=[[]for i in range(2*10**5+1)]
    dy=[[]for i in range(2*10**5+1)]
    s=[]
    ds=[]
    for i in range(1,1+n):
        a,b=map(int,input().split())
        infants.append([a,b])
        heapq.heappush(y[b],-a)
    for i in range(1,2*10**5+1):
        if y[i]:
            heapq.heappush(s,-y[i][0])
    for _ in range(q):
        c,d2=map(int,input().split())
        rate,d1=infants[c]
        heapq.heappush(dy[d1],-rate)
        heapq.heappush(ds,-y[d1][0])
        if y[d2]:
            heapq.heappush(ds,-y[d2][0])
        heapq.heappush(y[d2],-rate)
        if dy[d1]:
            while y[d1][0]==dy[d1][0]:
                heapq.heappop(y[d1])
                heapq.heappop(dy[d1])
                if not dy[d1]:
                    break
        if y[d1]:
            heapq.heappush(s,-y[d1][0])
        heapq.heappush(s,-y[d2][0])
        if ds:
            while ds and s[0]==ds[0]:
                heapq.heappop(s)
                heapq.heappop(ds)
                if not ds:
                    break
        infants[c][1]=d2
        print(s[0])
if __name__ == '__main__':
    main()