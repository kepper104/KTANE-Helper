import tkinter
from tkinter import CallWrapper, ttk
from tkinter.ttk import Checkbutton
from tkinter import messagebox
from tkinter import BooleanVar

confirmed = False
car = False
frk = False
carstate = 'Выключено'
frkstate = 'Выключено'
wiresList = []
blueCount = 0
redCount = 0
yellowCount = 0
whiteCount = 0


def quit(w):
    w.destroy()

def moduleSort(module):
    if confirmed == True:
        moduleActual = module.get()
        defuseWindow(moduleActual)
    else:
        notConfirmed()

def notConfirmed():
    messagebox.showerror("Error", "Вы не ввели переменные")


def valConfig():
    confWindow = tkinter.Tk()
    confWindow.title('Val Config')
    confWindow["bg"] = "lightgray"


    # global car
    # car = tkinter.BooleanVar()
    # car.set(0)
    
    def carFunc():
        global car
        global carstate
        if car == False:
            carstate = 'Включено'
            car = True
            carStateLbl['text'] = carstate
        else:
            carstate = 'Выключено'
            car = False
            carStateLbl['text'] = carstate
        print(car)
    def frkFunc():
        global frk
        if frk == False:
            frkstate = 'Включено'
            frk = True
            frkStateLbl['text'] = frkstate
        else:
            frkstate = 'Выключено'
            frk = False
            frkStateLbl['text'] = frkstate
        print(frk)


    lbl = tkinter.Label(confWindow,text='Настройка переменных',bg='lightgray')
    lbl.grid(row=1,column=1,padx=5)

    lastDigitLbl = tkinter.Label(confWindow,text='Последняя цифра сер. номера:',bg='lightgray')
    lastDigitLbl.grid(row=2,column=1,padx=5,pady=5)

    lastDigit = tkinter.Spinbox(confWindow,from_=0,to=9,width=5)
    lastDigit.grid(row=3,column=1,padx=5)

    batteriesLbl = tkinter.Label(confWindow,text='Количество батареек',bg='lightgray')
    batteriesLbl.grid(row=4,column=1,padx=5,pady=5)

    batteriess = tkinter.Spinbox(confWindow,from_=0,to=4,width=5)
    batteriess.grid(row=5,column=1,padx=5)
    
    # check1 = tkinter.Checkbutton(confWindow,text='Индикатор CAR',variable=car,onvalue=1, offvalue=0,command=carFunc)
    # check1.grid(row=6,column=1,padx=5,pady=5)

    # lastDigitLbl = tkinter.Label(confWindow,text='Нажмите если индикаторы горят',bg='lightgray')
    # lastDigitLbl.grid(row=6,column=1,padx=5,pady=5)

    btnConfirm = tkinter.Button(confWindow,text='Индикатор CAR',command=carFunc)
    btnConfirm.grid(row=7,column=1,padx=5,pady=5)

    carStateLbl = tkinter.Label(confWindow,text=carstate,bg='lightgray')
    carStateLbl.grid(row=8,column=1,padx=5)


    btnConfirm = tkinter.Button(confWindow,text='Индикатор FRK',command=frkFunc)
    btnConfirm.grid(row=7,column=1,padx=5,pady=5)
    btnConfirm.grid(row=9,column=1,padx=5)

    frkStateLbl = tkinter.Label(confWindow,text=frkstate,bg='lightgray')
    frkStateLbl.grid(row=10,column=1,padx=5)

    def valconfirm():
        global lastdigit
        global confirmed
        global car
        global frk
        global batteries
        confirmed = True
        lastdigit = lastDigit.get()
        batteries = batteriess.get()
        print(lastdigit)
        print(batteries)
        print(car)
        print(frk)
        quit(confWindow)


    btnConfirm = tkinter.Button(confWindow,text='Подтвердить',command=valconfirm)
    btnConfirm.grid(row=11,column=1,padx=5,pady=5)

def defuseWindow(moduleActual):
    
    if moduleActual == 'Провода':
        wires = tkinter.Tk()
        wires.title('Провода')
        wires['bg'] = 'lightgray'

        
        wiresLbl = tkinter.Label(wires,text='Введите провода в таком же порядке',font=("Arial Bold", 15),bg='lightgray')
        wiresLbl.grid(row=1,column=1,sticky='w')
        wiresLbl1 = tkinter.Label(wires,text='как и в игре(но без пропусков):',font=("Arial Bold", 15),bg='lightgray')
        wiresLbl1.grid(row=2,column=1,sticky='n')
        btnClsWires = tkinter.Button(wires,text='Закрыть',command=lambda: quit(wires))
        btnClsWires.grid(row=11,column=1,sticky='n',padx=120,pady=5)
        wire1 = ttk.Combobox(wires,width=20,state="readonly")
        wire1['values'] = ('Желтый','Красный','Синий','Черный','Белый',)
        wire1.set('Пусто')
        wire1.grid(row=3,column=1,sticky='n')
        wire2 = ttk.Combobox(wires,width=20,state="readonly")
        wire2['values'] = ('Желтый','Красный','Синий','Черный','Белый')
        wire2.set('Пусто')
        wire2.grid(row=4,column=1,sticky='n')
        wire3 = ttk.Combobox(wires,width=20,state="readonly")
        wire3['values'] = ('Желтый','Красный','Синий','Черный','Белый')
        wire3.set('Пусто')
        wire3.grid(row=5,column=1,sticky='n')
        wire4 = ttk.Combobox(wires,width=20,state="readonly")
        wire4['values'] = ('Желтый','Красный','Синий','Черный','Белый','Пусто')
        wire4.set('Пусто')
        wire4.grid(row=6,column=1,sticky='n')
        wire5 = ttk.Combobox(wires,width=20,state="readonly")
        wire5['values'] = ('Желтый','Красный','Синий','Черный','Белый','Пусто')
        wire5.set('Пусто')
        wire5.grid(row=7,column=1,sticky='n')
        wire6 = ttk.Combobox(wires,width=20,state="readonly")
        wire6['values'] = ('Желтый','Красный','Синий','Черный','Белый','Пусто')
        wire6.set('Пусто')
        wire6.grid(row=8,column=1,sticky='n')

        def wireCut(wire0):
            text1 = ('Режьте',wire0,'провод')
            wiresLbl2.config(text = text1)

        def wiresCount(l):
            global blueCount,redCount,yellowCount,whiteCount
            blueCount = 0
            redCount = 0
            yellowCount = 0
            whiteCount = 0
            print(l)
            for i in l:
                if i == 'Синий':
                    blueCount += 1
                elif i == 'Красный':
                    redCount += 1
                elif i == 'Желтый':
                    yellowCount += 1
                elif i == 'Белый':
                    whiteCount += 1
            if len(l) == 3:

                if 'Красный' not in l:
                    wireToCut = 'второй'
                    wireCut(wireToCut)

                elif l[2] == 'Белый':
                    wireToCut = 'последний'
                    wireCut(wireToCut)
                
                elif blueCount >= 2:
                    wireToCut = 'последний синий'
                    wireCut(wireToCut)
                else:
                    wireToCut = 'последний'
                    wireCut(wireToCut)
            elif len(l) == 4:
                if redCount >= 2 and int(lastdigit) % 2 != 0:
                    wireToCut = 'последний красный'
                    wireCut(wireToCut)
                elif l[3] == 'Желтый' and 'Красный' not in l:
                    wireToCut = 'первый'
                    wireCut(wireToCut)
                elif blueCount == 1:
                    wireToCut = 'первый'
                    wireCut(wireToCut)
                elif yellowCount >= 2:
                    wireToCut = 'последний'
                    wireCut(wireToCut)
                else:
                    wireToCut = 'второй'
                    wireCut(wireToCut)
            elif len(l) == 5:
                if l[4] == 'Черный' and int(lastdigit) % 2 != 0:
                    wireToCut = 'четвертый'
                    wireCut(wireToCut)
                elif redCount == 1 and yellowCount >= 2:
                    wireToCut = 'первый'
                    wireCut(wireToCut)
                elif 'Черный' not in l:
                    wireToCut = 'второй'
                    wireCut(wireToCut)
                else:
                    wireToCut = 'первый'
                    wireCut(wireToCut)
            elif len(l) == 6:
                if 'Желтый' not in l and int(lastdigit) % 2 != 0:
                    wireToCut = 'третий'
                    wireCut(wireToCut)
                elif yellowCount == 1 and whiteCount >= 2:
                    wireToCut = 'четвертый'
                    wireCut(wireToCut)
                elif 'Красный' not in l:
                    wireToCut = 'последний'
                    wireCut(wireToCut)
                else:
                    wireToCut = 'четвертый'
                    wireCut(wireToCut)
            else:
                wiresLbl2.config(text = "Ошибка")
                    






            # if w4 == 'Пусто' and w5 == 'Пусто' and w6 == 'Пусто':
            #     if w1 != 'Красный' and w2 != 'Красный' and w3 != 'Красный':
            #         wireToCut = 'второй'
            #         wireCut(wireToCut)
                
            #     elif w3 == 'Белый':
            #         wireToCut = 'последний'
            #         wireCut(wireToCut)
                   
            #     elif (w1 == 'Синий' and w2 == 'Синий') or (w1 == 'Синий' and w3 == 'Синий') or (w2 == 'Синий' and w3 == 'Синий'):
            #         wireToCut = 'последний синий'
            #         wireCut(wireToCut)
                   
            #     else:
            #         wireToCut = 'последний'
            #         wireCut(wireToCut)
            # elif w5 == 'Пусто' and w6 == 'Пусто':
            #     if ((w1 == 'Красный' and w2 == 'Красный') or (w1 == 'Красный' and w3 == 'Красный') or (w1 == 'Красный' and w4 == 'Красный') or (w2 == 'Красный' and w3 == 'Красный')  or (w3 == 'Красный' and w4 == 'Красный') or (w2 == 'Красный' and w4 == 'Красный')) and int(lastdigit) % 2 != 0:
            #         wireToCut = 'последний красный'
            #         wireCut(wireToCut)
            #     elif w4 == ' Желтый' and w1 != 'Красный' and w2 != 'Красный' and w3 != 'Красный' and w4 != 'Красный':
            #         wireToCut = 'первый'
            #         wireCut(wireToCut)
                    
                






            
        def wiresSort(a,b,c,d,e,f):
            # global wiresList
            wiresList = []
            wire1A = a.get()
            wire2A = b.get()
            wire3A = c.get() 
            wire4A = d.get()
            wire5A = e.get()
            wire6A = f.get()
            wiresList.append(wire1A)
            wiresList.append(wire2A)
            wiresList.append(wire3A)
            if wire4A == 'Пусто':
                pass
            else:
                wiresList.append(wire4A)

            if wire5A == 'Пусто':
                pass
            else:
                wiresList.append(wire5A)

            if wire6A == 'Пусто':
                pass
            else:
                wiresList.append(wire6A)
            wiresCount(wiresList)

         
        wiresLbl2 = tkinter.Label(wires,text='',font=("Arial Bold", 15),bg='lightgray')
        wiresLbl2.grid(row=10,column=1,sticky='n')

        btnWires = tkinter.Button(wires,text='Ввод',command=lambda: wiresSort(wire1,wire2,wire3,wire4,wire5,wire6))
        btnWires.grid(row=9,column=1,rowspan=1,sticky='n',padx=75,pady=5) 

        wires.mainloop()
    elif moduleActual == 'Кнопка':
        buttonWin = tkinter.Tk()
        buttonWin.title('Кнопка')
        buttonWin['bg'] = 'lightgray'
        clr = tkinter.StringVar()
        lbl = tkinter.StringVar()

        def holding():
            tkinter.Label(buttonWin,text='----------------',font=("Arial Bold", 15),bg='lightgray').grid(row=13,column=1)
            tkinter.Label(buttonWin,text='Если полоска синяя:',font=("Arial Bold", 15),bg='lightgray').grid(row=14,column=1)
            tkinter.Label(buttonWin,text='Отпустите, когда на таймере 4.',font=("Arial Bold", 15),bg='lightgray').grid(row=15,column=1)
            tkinter.Label(buttonWin,text='Если полоска желтая',font=("Arial Bold", 15),bg='lightgray').grid(row=16,column=1)
            tkinter.Label(buttonWin,text='Отпустите, когда на таймере 5.',font=("Arial Bold", 15),bg='lightgray').grid(row=17,column=1)
            tkinter.Label(buttonWin,text='Если полоска другого цвета',font=("Arial Bold", 15),bg='lightgray').grid(row=18,column=1)
            tkinter.Label(buttonWin,text='Отпустите, когда на таймере 1.',font=("Arial Bold", 15),bg='lightgray').grid(row=19,column=1)

        def btnSort(c,l):
            if c == 'Синяя':
                result['text'] = 'Удерживайте,'
                holding()
            elif int(batteries) >= 2 and l == 'Взорвать':
                result['text'] = 'Резко нажмите и отпустите'
            elif c == 'Белая' and car == True:
                result['text'] = 'Удерживайте,'
                holding()
            elif int(batteries) >= 3 and frk == True:
                result['text'] = 'Резко нажмите и отпустите'
            elif c == 'желтая':
                result['text'] = 'Удерживайте,'
                holding()
            elif c == 'Красная' and l == 'Держать':
                result['text'] = 'Резко нажмите и отпустите'
            else:
                result['text'] = 'Удерживайте,'
                holding()

        tkinter.Label(buttonWin,text='Цвет кнопки:',font=("Arial Bold", 15),bg='lightgray').grid(row=1,column=1)
        colorCombo = ttk.Combobox(buttonWin,width=20,textvariable=clr,state="readonly")
        colorCombo['values'] = ('Синяя','Белая','Желтая','Красная','Другая')
        colorCombo.set('Выберите цвет')
        colorCombo.grid(row=2,column=1,rowspan=2,pady=5)
        tkinter.Label(buttonWin,text='Надпись на кнопке:',font=("Arial Bold", 15),bg='lightgray').grid(row=5,column=1)
        labelCombo = ttk.Combobox(buttonWin,width=20,textvariable=lbl,state="readonly")
        labelCombo['values'] = ('Прервать','Взорвать','Держать','Другое')
        labelCombo.set('Выберите надпись')
        labelCombo.grid(row=7,column=1,rowspan=2,pady=5)
        btnBtn = tkinter.Button(buttonWin,text='Подтвердить',command=lambda: btnSort(clr,lbl))
        btnBtn.grid(row=10,column=1,rowspan=2,pady=5)

        result = tkinter.Label(buttonWin,text='',font=("Arial Bold", 15),bg='lightgray')
        result.grid(row=12,column=1)

        buttonWin.mainloop()
    

def makeRoot():
    root = tkinter.Tk()
    root.title('Обезвреживание бомб')
    root["bg"] = "lightgray"

    operatingModule = tkinter.StringVar()

    tkinter.Label(root,text='Выберите модуль:',font=("Arial Bold", 30),bg='lightgray').grid(row=1,column=1)

    combobox = ttk.Combobox(root,width=20,textvariable=operatingModule,state="readonly")
    combobox['values'] = ('Провода','Кнопка','Память')
    combobox.set('Провода')
    combobox.grid(row=2,column=1,rowspan=2,pady=5)

    btn = tkinter.Button(root,text='Начать Обезвреживание!',command=lambda: moduleSort(operatingModule))
    btn.grid(row=4,column=1,rowspan=2,pady=5)

    btnConf = tkinter.Button(root,text='Ввод Переменных',command=valConfig)
    btnConf.grid(row=6,column=1,pady=5)

    btnCls = tkinter.Button(root,text='Закрыть',command=lambda: quit(root))
    btnCls.grid(row=7,column=1,pady=5)

    root.mainloop()

makeRoot()
