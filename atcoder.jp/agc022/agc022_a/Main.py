s=input()

ll=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

if len(s)!=26:
    l=list(s)
    for i in l:
        ll.remove(i)
    ll.sort()
    print(s+ll[0])
else:
    if s=="zyxwvutsrqponmlkjihgfedcba":
        print(-1)
    else:
        l=[]
        for i in range(1,27):
            for j in l:
                if s[-i]<j:
                    print(s[0:26-i]+j)
                    import sys
                    sys.exit()
            l.append(s[-i])
            l.sort()
            