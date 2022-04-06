print('введіть текст')
bred = str(input())          
while bred.find('  ') != -1:
    bred = bred.replace('  ', ' ')
print('введіть бажану довжину слова')
dovj = int(input())         
sl = ''
n = 0
n_slova = 0
while n<=len(bred):
    if bred[n]!=' ':
        sl = sl + str (bred[n])
        if n==(len(bred)-1):
            if dovj==len(sl):
                n_slova += 1
                print ('Слово номер ' + str(n_slova) + ': '+(sl))
        n+=1
    elif bred[n]==' ':
        n_slova += 1
        if dovj==len(sl):
            print ('Слово номер ' + str(n_slova) + ': '+(sl))
        sl = ''
        n+=1  



