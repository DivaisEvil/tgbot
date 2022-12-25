a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if(a1<=a2<b1<b2):
    print(a2,b1, sep=' ')
elif(a2<a1<b2<b1):
    print(a1,b2, sep=' ')
elif(a1<a2<b2<=b1):
    print(a2,b2, sep=' ')
elif(a2<a1<b1<=b2):
    print(a1,b1, sep=' ')
elif(a1==a2 and b1 == b2):
    print(a1,b1, sep=' ')
elif(a1<b1==a2<b2):
    print(b1)
elif a1<a2<b1<b2:
    print(a2,b1, sep=' ')
elif b2<a2==b1<a2:
    print(b1)
else:
    print('пустое множество')