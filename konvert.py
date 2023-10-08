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
List_note_text1 = QLabel('Категория:')
List_note = QListWidget()
List_note_text2 = QLabel('Исходная величина:')
List_note = QListWidget()
List_note_text3 = QLabel('Конечная величина:')
List_note = QListWidget()

list_cut = QComboBox()
list_cut.addItems(['Длина', 'Масса', 'Время', 'Скорость', 'Давление'])
list_ishodnoe = QComboBox()

list_initival_S=['Км', 'М', 'Дм', 'См', 'Мм']
list_initival_m=['Т', 'Ц', 'Кг', 'Г', 'Мг']
list_initival_t=['Неделя', 'Сутки', 'Час', 'Мин', 'Сек']
# list_initival_v=['Т', 'Ц', 'Кг', 'Г', 'Мг']

def pokazat():
    if list_cut.count() == 0:
        list_ishodnoe.deleteLater()
        list_ishodnoe.addItems(list_initival_S)
    # if list_cut.count() == 1:
    else:
        list_ishodnoe.deleteLater()
        list_ishodnoe.addItems(list_initival_m)


# list_initival_S = QComboBox()

# list_initival_m = QComboBox()

# list_initival_t = QComboBox()

# list_initival_v = QComboBox()





btn_0 = QPushButton('0')
btn_1 = QPushButton('1')
btn_2 = QPushButton('2')
btn_3 = QPushButton('3')
btn_4 = QPushButton('4')
btn_5 = QPushButton('5')
btn_6 = QPushButton('6')
btn_7 = QPushButton('7')
btn_8 = QPushButton('8')
btn_8 = QPushButton('9')
comm = QPushButton(',')
back = QPushButton('CE')
dell = QPushButton('Delete')
tran = QPushButton('Перевести')

q1 = QHBoxLayout()
q2 = QHBoxLayout()
q3 = QHBoxLayout()
q1.addWidget(list_cut)
q1.addWidget(list_ishodnoe)
q2.addWidget(tran)

main_Layout = QVBoxLayout()
main_Layout.addLayout(q1)
main_Layout.addLayout(q2)

MainWin.setLayout(main_Layout)

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



tran.clicked.connect(pokazat)


MainWin.show()
app.exec_()
