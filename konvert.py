from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
                            QApplication, QWidget, QPushButton,
                            QLabel, QListWidget, QLineEdit, QTextEdit,
                            QVBoxLayout, QHBoxLayout,QInputDialog, QComboBox
                            )

app = QApplication([])
MainWin = QWidget()
MainWin.setWindowTitle('Конвертер')
MainWin.resize(500,400)

Text = QTextEdit()
text_Kategory = QLabel('Категория:')
text_ishodnoe = QLabel('Исходная величина:')
text_konechnaya = QLabel('Конечная величина:')

digit_text = QTextEdit()

list_cut = QComboBox()
list_ishodnoe = QComboBox()
List_konechnaya = QComboBox()

list_cut.addItems(['Длина', 'Масса', 'Время', 'Давление'])

d = ['Километр', 'Mетр', 'Сантиметр']
mm = ['Tонна', 'Kилограмм', 'грамм']
t = [ 'Сутки', 'Час', 'Минута', ]
p =  ['Па', 'кПа', 'мПа']

def qq():
    if list_cut.currentText() == 'Длина':
        list_ishodnoe.clear()
        list_ishodnoe.addItems(d)
        List_konechnaya.clear()
        List_konechnaya.addItems(d)
    if list_cut.currentText() == 'Масса':
        list_ishodnoe.clear()
        list_ishodnoe.addItems(mm)
        List_konechnaya.clear()
        List_konechnaya.addItems(mm)
    if list_cut.currentText() == 'Время':
        list_ishodnoe.clear()
        list_ishodnoe.addItems(t)
        List_konechnaya.clear()
        List_konechnaya.addItems(t)
    if list_cut.currentText() == 'Давление':
        list_ishodnoe.clear()
        list_ishodnoe.addItems(p)
        List_konechnaya.clear()
        List_konechnaya.addItems(p)

list_cut.activated.connect(qq)
qq()

btn_0 = QPushButton('0')
btn_1 = QPushButton('1')
btn_2 = QPushButton('2')
btn_3 = QPushButton('3')
btn_4 = QPushButton('4')
btn_5 = QPushButton('5')
btn_6 = QPushButton('6')
btn_7 = QPushButton('7')
btn_8 = QPushButton('8')
btn_9 = QPushButton('9')
comm = QPushButton('.')
back = QPushButton('CE')
dell = QPushButton('Delete')
tran = QPushButton('Перевести')

q1 = QVBoxLayout()
q1.addWidget(text_Kategory)
q1.addWidget(list_cut, stretch=0, alignment=Qt.AlignTop)
q1.addWidget(text_ishodnoe)
q1.addWidget(list_ishodnoe, stretch=0, alignment=Qt.AlignTop)
q1.addWidget(text_konechnaya)
q1.addWidget(List_konechnaya, stretch=0, alignment=Qt.AlignTop)
q1.addWidget(tran)

q2 = QVBoxLayout()
q2.addWidget(digit_text)
digit_line0 = QHBoxLayout()
digit_line1 = QHBoxLayout()
digit_line2 = QHBoxLayout()
digit_line3 = QHBoxLayout()
digit_line4 = QHBoxLayout()

digit_line0.addWidget(btn_0)
digit_line0.addWidget(comm)
digit_line1.addWidget(btn_7)
digit_line1.addWidget(btn_8)
digit_line1.addWidget(btn_9)
digit_line2.addWidget(btn_4)
digit_line2.addWidget(btn_5)
digit_line2.addWidget(btn_6)
digit_line3.addWidget(btn_1)
digit_line3.addWidget(btn_2)
digit_line3.addWidget(btn_3)
digit_line4.addWidget(back)
digit_line4.addWidget(dell)

q2.addLayout(digit_line4) 
q2.addLayout(digit_line3)
q2.addLayout(digit_line2) 
q2.addLayout(digit_line1) 
q2.addLayout(digit_line0) 

q_main = QHBoxLayout()
q_main.addLayout(q1)
q_main.addLayout(q2)

MainWin.setLayout(q_main)

text = ''
def click_1():
    global text
    text += '1'
    digit_text.setText(text)
def click_2():
    global text
    text += '2'
    digit_text.setText(text)
def click_3():
    global text
    text += '3'
    digit_text.setText(text)
def click_4():
    global text
    text += '4'
    digit_text.setText(text)
def click_5():
    global text
    text += '5'
    digit_text.setText(text)
def click_6():
    global text
    text += '6'
    digit_text.setText(text)
def click_7():
    global text
    text += '7'
    digit_text.setText(text)
def click_8():
    global text
    text += '8'
    digit_text.setText(text)
def click_9():
    global text
    text += '9'
    digit_text.setText(text)
def click_0():
    global text
    text += '0'
    digit_text.setText(text)
def click_comm():
    global text
    text += '.'
    digit_text.setText(text)
def click_back():
    global text
    text = text[:-1]
    digit_text.setText(text)
def click_dell():
    global text
    text = ''
    digit_text.setText(text)

#Длина

def mb(digit): #из км в м
    m = digit*1000
    return m
def Sm(digit): #из км в см
    sm = digit*1000000
    return sm
def smm(digit): #из см в м
    smm = digit/100
    return smm
def Smk(digit): #из см в км
    smk = digit/1000000
    return smk
def mk(digit): #из м в км
    mk = digit/1000
    return mk
def mSm(digit): #из м в см
    mSm = digit*100
    return mSm

#Масса

def Kg(digit): #из т в кг
    Kg = digit*1000
    return Kg    
def g(digit): #из т в г
    g = digit*1000000
    return g   
def T(digit): #из кг в т
    T = digit/1000
    return T     
def kgg(digit): #из кг в г
    kgg = digit*1000
    return kgg     
def gt(digit): #из г в т
    gt = digit/1000000
    return gt    
def gk(digit): #из г в кг
    gk = digit/1000
    return gk     

#Время

def dh(digit): # сутки в часы
    dh = digit*24
    return dh
def m(digit): # сутки в минуты
    m = digit*1440
    return m
def hd(digit): # часы в сутки
    hd = digit/24
    return hd
def hm(digit): # часы в минуты
    hm = digit*60
    return hm
def md(digit): # из минут в сутки
    md = digit/1440
    return md
def mh(digit): # из минут в часы
    mh = digit/60
    return mh

#Давление

def kPa(digit): # паскали в кПа
    kPa = dict/1000
    return kPa
def mPa(digit): # Па мПа
    mPa = digit/1000000
    return mPa
def Pa(digit): # кПа в Па
    Pa = digit*1000
    return Pa
def kmPa(digit): # кПа в мПа
    kmPa = digit/1000
    return kmPa
def mkPa(digit): #мПа в кПа
    mkPa = digit*1000
    return mkPa
def Pam(digit): # мПа в Па
    Pam = digit*1000000
    return Pam


btn_1.clicked.connect(click_1)
btn_2.clicked.connect(click_2)
btn_3.clicked.connect(click_3)
btn_4.clicked.connect(click_4)
btn_5.clicked.connect(click_5)
btn_6.clicked.connect(click_6)
btn_7.clicked.connect(click_7)
btn_8.clicked.connect(click_8)
btn_9.clicked.connect(click_9)
btn_0.clicked.connect(click_0)
comm.clicked.connect(click_comm)
back.clicked.connect(click_back)
dell.clicked.connect(click_dell)

def dalhe(digit): 
    if list_ishodnoe.currentText() == 'Километр':
        if List_konechnaya.currentText() == 'Mетр':
            z = mb(digit)
            return z
        elif List_konechnaya.currentText() == 'Сантиметр':
            z = Sm(digit)
            return z
    elif list_ishodnoe.currentText() == 'Mетр':
        if List_konechnaya.currentText() == 'Километр':
            z = mk(digit)
            return z
        elif List_konechnaya.currentText() == 'Сантиметр':
            z = mSm(digit)
            return z
    elif list_ishodnoe.currentText() == 'Сантиметр':
        if List_konechnaya.currentText() == 'Километр':
            z = Smk(digit)
            return z
        elif List_konechnaya.currentText() == 'Mетр':
            z = smm(digit)
            return z
# ========================================================
    if list_ishodnoe.currentText() == 'Tонна':
        if List_konechnaya.currentText() == 'Kилограмм':
            z = Kg(digit)
            return z
        elif List_konechnaya.currentText() == 'грамм':
            z = g(digit)
            return z
    elif list_ishodnoe.currentText() == 'Kилограмм':
        if List_konechnaya.currentText() == 'Tонна':
            z = T(digit)
            return z
        elif List_konechnaya.currentText() == 'грамм':
            z = kgg(digit)
            return z
    elif list_ishodnoe.currentText() == 'грамм':
        if List_konechnaya.currentText() == 'Kилограмм':
            z = gk(digit)
            return z
        elif List_konechnaya.currentText() == 'Tонна':
            z = gt(digit)
            return z
# ========================================================    
    elif list_ishodnoe.currentText() == 'Сутки':
        if List_konechnaya.currentText() == 'Час':
            z = dh(digit)
            return z
        elif List_konechnaya.currentText() == 'Минута':
            z = m(digit)
            return z
    elif list_ishodnoe.currentText() == 'Час':
        if List_konechnaya.currentText() == 'Сутки':
            z = hd(digit)
            return z
        elif List_konechnaya.currentText() == 'Минута':
            z = hm(digit)
            return z
    elif list_ishodnoe.currentText() == 'Минута':
        if List_konechnaya.currentText() == 'Сутки':
            z = md(digit)
            return z
        elif List_konechnaya.currentText() == 'Час':
            z = mh(digit)
            return z

# ========================================================    
    elif list_ishodnoe.currentText() == 'Па':
        print("зашли в ПА")
        if List_konechnaya.currentText() == 'кПа':
            z = kPa(digit)
            return z
        elif List_konechnaya.currentText() == 'мПа':
            z = mPa(digit)
            return z
    elif list_ishodnoe.currentText() == 'кПа':
        if List_konechnaya.currentText() == 'Па':
            z = Pa(digit)
            return z
        elif List_konechnaya.currentText() == 'мПа':
            z = kmPa(digit)
            return z
    elif list_ishodnoe.currentText() == 'мПа':
        if List_konechnaya.currentText() == 'кПа':
            z = mkPa(digit)
            return z
        elif List_konechnaya.currentText() == 'Па':
            z = Pam(digit)
            return z

def go():
    global text
    try:
        print(0)
        digit = float(text)
        print(1)
        c = dalhe(digit)
        print(2)
        digit_text.setText(str(c))
    except:
        digit_text.setText('Не число введено')

tran.clicked.connect(go)

MainWin.show()
app.exec_()
