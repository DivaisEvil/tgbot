a = int(input())

for i in range(1,a+1):
    #print(i, end='')
    for c in range(1,a):
        print(c,end='')
    for s in range(1,i,i+1):
        print(s,end='')
    for j in range(i - 1, 0, -1):
        print(j,end='')
    #for k in range(i-1,0,-1):
       # print(k,end='')

    print()