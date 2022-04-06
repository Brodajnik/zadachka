#імпортуємо модуль import PySimpleGUI as sg для роботи графіки.
#Встановлення:
#apt install python3-pip python3-tk
#pip3 install PySimpleGUI
#Виникли трабли з залежностями, рішення:
#apt update
#apt --fix-broken install

import re
import PySimpleGUI as sg #імпортуємо графічний модуль PySimpleGUI
layout = [
    [sg.Text('Введіть текст               '), sg.InputText(key='-IN-'), sg.Cancel('Очистити')],
    [sg.Text('Введіть довжину слова'), sg.InputText(key='-IN2-'), sg.Submit('Запустити')],
    [sg.Output(size=(88, 20), key='-OUT-')],
]
window = sg.Window('задача', layout)        #створили вікно та його назву
while True:                                 #власне, запустили графу
    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):   #закрити вікно
        break                               #де-факто вікно - цикл, закрити - брейк
    if event == 'Запустити':                #власне, запуск проги
        bred = str(values['-IN-'])          #присвоюємо змінній введене значення та тип 'стр'
        bred = re.sub(r'\s+', ' ', bred)    #забираємо зайві пробіли (модуль 're')
        dovj = int(values['-IN2-'])         #присвоюємо змінній введене значення та тип 'інт'
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
                    n_slova += 1
                    print ('Слово номер ' + str(n_slova) + ': '+(sl))
                sl = ''
                n+=1
    if event == 'Очистити':                 #очищення вікна
        window['-OUT-'].update('')

