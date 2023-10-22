from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
                            QApplication, QWidget, QPushButton,
                            QLabel, QListWidget, QLineEdit, QTextEdit,
                            QVBoxLayout, QHBoxLayout,QInputDialog, QComboBox
                            )

app = QApplication([])
MainWin = QWidget()
MainWin.setWindowTitle('Конвертер')
MainWin.resize(900,700)
Text = QTextEdit()
text_Kategory = QLabel('Категория:')
# List_note = QListWidget()
text_ishodnoe = QLabel('Исходная величина:')
# List_note = QListWidget()
text_konechnaya = QLabel('Конечная величина:')
# List_note = QListWidget()

digit_text = QTextEdit()

list_cut = QComboBox()
list_cut.addItems(['Длина', 'Масса', 'Время', 'Давление'])

list_ishodnoe = QComboBox()
List_konechnaya = QComboBox()

d = ['Километр ', 'Mетр', 'Сантиметр']
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
#Длина
def m(digit): #из км в м
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




# if list_cut.count() == 0:
#     list_ishodnoe.addItems(list_initival_S)



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
comm = QPushButton(',')
back = QPushButton('CE')
dell = QPushButton('Delete')

tran = QPushButton('Перевести')

q1 = QVBoxLayout()
q1.addWidget(text_Kategory)
q1.addWidget(list_cut)
q1.addWidget(text_ishodnoe)
q1.addWidget(list_ishodnoe)
q1.addWidget(text_konechnaya)
q1.addWidget(List_konechnaya)
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
'''
def show_note():
    name = List_note.selectedItems()[0].text()
    Text.setText(notes[name]['текст'])
    LIst_tag.clear()
    List_tag.addItems(notes[name]['теги'])

def add_none():
    note_name, ok = QInputDialog.getText('Добавить', 'Название заметки')
    if ok and note_name != '':
        notes[note_name] = {'текст': '', 'теги': []}
        List_note.addItem(note_name)
        List_tag.addItem(notes[note_name]['теги'])

def delit_note():
    if List_note.selectedItems():
        key = List_note.selectedItems()[0].text()
        del notes[key]
        with open('notes.json' , 'w' , encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True)

def SaveNote():
    if List_note.selectedItems():
        key = List_note.selectedItems()[0].text()
        notes[key]['текст'] = Text.toPlainText()

    with open('notes.json' , 'w' , encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True)

def addTag():
    if List_note.selectedItems():
        key = List_note.selectedItems()[0].text()
        Tag = tag.text()
        if Tag in notes[key]['теги']:
            notes[key]['теги'].append(Tag)
            List_tag.addItem(Tag)
            tag.clear()
        with open('notes.json' , 'w' , encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True)
        
def delTag():
    if List_note.selectedItems():
        key = List_note.selectedItems()[0].text()
        Tag = List_note.selectedItems()[0].text()
        notes[key]['теги'].remove(tag)
        with open('notes.json' , 'w' , encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True)
        
def searchTag():
    Tag = tag.text()
    if search_tag.text() == 'Искать заметки по тегу':
        filter_notes = {}
        for njte in notes:
            if Tag in notes[note]['теги']:
                filter_notes[note] =  notes[note]
        search_tag.setText('Сбросить')      
        tag.clear()
        List_note.clear()
        List_tag.clear()
        List_note.addItems(filter_notes)
    elif search_tag.text() == 'Сбросить':
        tag.clear()
        List_note.clear()
        List_tag.clear()
        List_note.addItems(notes)
        search_tag.setText('Искать заметки по тегу')
'''




tran.clicked.connect(qq)

MainWin.show()
app.exec_()
