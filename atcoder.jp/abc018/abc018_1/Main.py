l=[int(input())for i in range(3)]
a_to_i={a:i for i,a in enumerate(sorted(set(l),reverse=True),1)}
for a in l:
    print(a_to_i[a])