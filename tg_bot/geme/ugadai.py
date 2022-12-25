'''ru=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] #
#ru=['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
rum=[]
for i in ru:
    rum.append(i.lower())

#print(ru,rum)
def rel(k,s):
    q=''
    for i in s:
        if i.isalpha()==False:
            q+=i
            continue
        if i ==i.upper():
            cur_index = ru.index(i)
            new_index = cur_index + k
            if new_index > len(ru) - 1:
                new_index = new_index - len(ru)
            if new_index<0:
                new_index=new_index+len(ru)
            q+= ru[new_index]

        else:
            cur_index = rum.index(i)
            new_index = cur_index + k
            if new_index > len(rum) - 1:
                new_index = new_index - len(rum)
            if new_index<0:
                new_index=new_index+len(rum)
            q += rum[new_index]

    return q
w=input()
result=''
word=''
for i in w:
    if i.isalpha() == False:
        if len(word) > 0:
            result += rel(len(word), word)
            word=''
        result += i
        continue
    else:
        word+=i
if len(word)>0:
    result+=rel(len(word),word)
print(result)




import random

def start():
    print('введите число от 1 до 100')
    return input()

print('Добро пожаловать в числовую угадайку (ot 0 do 100)')
x = random.randrange(101)
znak=''
while znak.isdigit()!=True or 1>int(znak) or int(znak)>100:
    znak=start()'''
print('{0:b}'.format(513))
