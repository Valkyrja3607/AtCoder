import random
import math
import copy
import time

def read_input():
    n=int(input())
    l=[list(map(int,input().split()))for i in range(n)]
    return n,l

def eval_score(n, state, new_state, i, pre, l):
    pre*=n
    a,b,c,d=state[i]
    s=abs((a-c)*(b-d))
    pre-=1-(1-min(l[i][2],s)/max(l[i][2],s))**2
    a,b,c,d=new_state[i]
    s=abs((a-c)*(b-d))
    pre+=1-(1-min(l[i][2],s)/max(l[i][2],s))**2
    pre/=n

    return pre

def f(a,b):
    return max(a[0],b[0])<min(a[2],b[2]) and max(a[1],b[1])<min(a[3],b[3])

def SA(n,l):
    ut = time.time()
    now=0
    state = []
    for i,j,k in l:
        state.append([i,j,i+1,j+1])
    new_state = copy.deepcopy(state)
    ans = copy.deepcopy(state)
    tmp=0
    
    pre=0
    for i in range(n):
        pre+=1-(1-1/l[i][2])**2
    pre/=n
    s = 5000000
    cnt = s
    cc=0
    temp0, temp1 = 30, 10
    now=0
    while time.time()-ut<4.5:
        #new_state = copy.deepcopy(state)
        cnt -= 1
        temp = 0
        i = random.randint(0,n-1)
        j = random.randint(0,3)
        k = random.randint(1,5)
        if random.randint(0,9999)>1:
            if j>1:
                if state[i][j]+k<=10000:
                    new_state[i][j] = state[i][j]+k
                else:
                    continue
            else:
                if state[i][j]-k>=0:
                    new_state[i][j] = state[i][j]-k
                else:
                    continue
        else:
            if j>1:
                if state[i][j]-10>=0:
                    new_state[i][j] = (state[i][j]+(state[i][j]+state[i][(j+2)%4])//2)//2
                else:
                    continue
            else:
                if state[i][j]+10<=10000:
                    new_state[i][j] = (state[i][j]+(state[i][j]+state[i][(j+2)%4])//2)//2
                else:
                    continue
        
        bo=False
        for k in range(n):
            if i!=k and f(new_state[i],new_state[k]):
                new_state[i][j] = state[i][j]
                cc+=1
                bo=True
                break
        if bo:
            new_state[i][j] = state[i][j]
            #new_state = copy.deepcopy(state)
        elif new_state[i][0]<=l[i][0]<new_state[i][2] and new_state[i][1]<=l[i][1]<new_state[i][3]:
            new_score = eval_score(n, state, new_state, i, pre, l)
            if now>4 and tmp<new_score:
                tmp=new_score
                ans=copy.deepcopy(new_state)
            temp += temp0 + (temp1 - temp0) * (now/4.5)
            prob = math.exp((new_score - pre) / temp)
            if random.random() <= prob:
                pre = new_score
                state[i][j] = new_state[i][j]
            else:
                new_state[i][j] = state[i][j]
        else:
            new_state[i][j] = state[i][j]
        now=time.time()-ut
    #print(cc)
    return ans



def main():
    n,l = read_input()
    ans = SA(n,l)
    for a in ans: print(*a)
    

    

if __name__ == "__main__":
    """if sys.argv[-1] == 'ONLINE_JUDGE':
        from numba.pycc import CC
        from numba import njit
        cc = CC('my_module')
        funcs_and_sigs = [
            ('eval_score', 'i8(i8[:], i8[:,:], i8, i8)'),
            ('SA', 'i8[:,:](i8[:], i8[:,:], i8[:,:])')
        ]
        d = globals()
        for fname, sig in funcs_and_sigs:
            func = d[fname]
            cc.export(func.__name__, sig)(func)
            d[fname] = njit(func)
        cc.compile()
        exit()
    from my_module import *"""
    main()