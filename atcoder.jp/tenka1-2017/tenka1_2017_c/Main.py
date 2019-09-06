n=int(input())

for i in range(1,3501):
    for j in range(1,3501):
        if (4*i*j-n*i-n*j)>0 and float((n*i*j)/(4*i*j-n*i-n*j)).is_integer():
            print(i,j,int((n*i*j)/(4*i*j-n*i-n*j)))
            exit()







