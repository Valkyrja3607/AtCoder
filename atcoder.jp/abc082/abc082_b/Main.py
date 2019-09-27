s="".join(sorted(list(input())))
t="".join(reversed(sorted(list(input()))))
if s<t:
    print("Yes")
else:
    print("No")