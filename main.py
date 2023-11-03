import io
import random
import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox

color = 1
write = ''
correct = False
name = ''
k = 0
n = 0
f = open('noun.txt', encoding='utf8')
noun = f.readlines()
noun = [e.replace('\n', '') for e in noun]
noun = [x for x in noun if x != '']
noun[-1] = noun[-1][0:7]
f.close()
f = open('verb.txt', encoding='utf8')
verb = f.readlines()
verb = [e.split('\t')[1] for e in verb]
verb = [e.replace('\n', '') for e in verb]
verb = [x for x in verb if x != '']
f.close()
f = open('adj.txt', encoding='utf8')
adj = f.readlines()
adj = [e.split('\t')[1] for e in adj]
adj = [e.replace('\n', '') for e in adj]
adj = [x for x in adj if x != '']
f.close()
alll = noun + verb + adj
s = ''
language = ''

elements = []

class Type1Error(Exception):
    pass


class Type2Error(Exception):
    pass


class Type3Error(Exception):
    pass


class Type4Error(Exception):
    pass


class Type5Error(Exception):
    pass


class Type6Error(Exception):
    pass


class NotSameError(Exception):
    pass


class ElementNotInError(Exception):
    pass


class EmptyError(Exception):
    pass


class LengError(Exception):
    pass


class Notebook2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled1.ui", self)
        self.setWindowTitle("Выберите оформление и нажмите 'НАЧАТЬ'")
        self.radioButton_1.clicked.connect(self.change)
        self.radioButton_2.clicked.connect(self.change)
        self.radioButton_3.clicked.connect(self.change)
        self.radioButton_4.clicked.connect(self.change)
        self.start_but.clicked.connect(self.open_second_form)
        self.setStyleSheet("background-color: rgb(170, 200, 255)")

    def change(self):
        global color
        if self.sender() == self.radioButton_1:
            color = 1
            self.setStyleSheet("QMainWindow { background-color: rgb(204, 255, 204)}")
            self.start_but.setStyleSheet("background-color: rgb(255, 153, 204)")
            self.radioButton_1.setStyleSheet("background-color: rgb(255, 153, 204)")
            self.radioButton_2.setStyleSheet("background-color: rgb(255, 153, 204)")
            self.radioButton_3.setStyleSheet("background-color: rgb(255, 153, 204)")
            self.radioButton_4.setStyleSheet("background-color: rgb(255, 153, 204)")
        if self.sender() == self.radioButton_2:
            color = 2
            self.setStyleSheet("QMainWindow { background-color: rgb(255, 159, 172) }")
            self.start_but.setStyleSheet("background-color: rgb(255, 185, 135)")
            self.radioButton_1.setStyleSheet("background-color: rgb(255, 185, 135)")
            self.radioButton_2.setStyleSheet("background-color: rgb(255, 185, 135)")
            self.radioButton_3.setStyleSheet("background-color: rgb(255, 185, 135)")
            self.radioButton_4.setStyleSheet("background-color: rgb(255, 185, 135)")
        if self.sender() == self.radioButton_3:
            color = 3
            self.setStyleSheet("QMainWindow { background-color: rgb(170, 200, 255) }")
            self.start_but.setStyleSheet("background-color: rgb(170, 170, 255)")
            self.radioButton_1.setStyleSheet("background-color: rgb(170, 170, 255)")
            self.radioButton_2.setStyleSheet("background-color: rgb(170, 170, 255)")
            self.radioButton_3.setStyleSheet("background-color: rgb(170, 170, 255)")
            self.radioButton_4.setStyleSheet("background-color: rgb(170, 170, 255)")
        if self.sender() == self.radioButton_4:
            color = 4
            self.setStyleSheet("QMainWindow { background-color: rgb(255, 255, 153) }")
            self.start_but.setStyleSheet("background-color: rgb(255, 198, 85)")
            self.radioButton_1.setStyleSheet("background-color: rgb(255, 198, 85)")
            self.radioButton_2.setStyleSheet("background-color: rgb(255, 198, 85)")
            self.radioButton_3.setStyleSheet("background-color: rgb(255, 198, 85)")
            self.radioButton_4.setStyleSheet("background-color: rgb(255, 198, 85)")

    def open_second_form(self):
        self.second_form = Notebook1()
        self.second_form.show()


class Notebook1(Notebook2):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled.ui", self)
        self.bd_name = "noname.bd"
        self.setWindowTitle('Рандомайзер')
        global color
        self.color1 = (170, 200, 255)
        self.color2 = (170, 170, 255)
        self.color3 = (170, 230, 255)
        if color == 1:
            self.color1 = (204, 255, 204)
            self.color2 = (255, 153, 204)
            self.color3 = (234, 255, 203)
        if color == 2:
            self.color1 = (255, 159, 172)
            self.color2 = (255, 185, 135)
            self.color3 = (255, 189, 183)
        if color == 3:
            self.color1 = (170, 200, 255)
            self.color2 = (170, 170, 255)
        if color == 4:
            self.color1 = (255, 255, 153)
            self.color2 = (255, 198, 85)
            self.color3 = (255, 255, 183)
        self.setStyleSheet(f"background-color: rgb{self.color3}")
        self.tabWidget.setStyleSheet(f"background-color: rgb{self.color1}")
        self.tab_1.setStyleSheet(f"background-color: rgb{self.color1}")
        self.tab_7.setStyleSheet(f"background-color: rgb{self.color1}")
        self.diap.setStyleSheet(f"background-color: rgb{self.color2}")
        self.label_1.setStyleSheet(f"background-color: rgb{self.color2}")
        self.label_2.setStyleSheet(f"background-color: rgb{self.color2}")
        self.pushButton.setStyleSheet(f"background-color: rgb{self.color2}")
        self.noun_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.verb_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.adj_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.all_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.translate_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.element.setStyleSheet(f"background-color: rgb{self.color2}")
        self.add_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.del_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.clear_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.label_3.setStyleSheet(f"background-color: rgb{self.color2}")
        self.label_4.setStyleSheet(f"background-color: rgb{self.color2}")
        self.pushButton_2.setStyleSheet(f"background-color: rgb{self.color2}")
        self.pushButton_3.setStyleSheet(f"background-color: rgb{self.color2}")
        self.pushButton_4.setStyleSheet(f"background-color: rgb{self.color2}")
        self.cub_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.coin_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.rules_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.itog_but.setStyleSheet(f"background-color: rgb{self.color2}")
        self.pushButton_7.setStyleSheet(f"background-color: rgb{self.color2}")
        self.pushButton_6.setStyleSheet(f"background-color: rgb{self.color2}")
        self.tabWidget.setTabText(0, 'Число')
        self.tabWidget.setTabText(1, 'Слово')
        self.tabWidget.setTabText(2, 'Элемент списка')
        self.tabWidget.setTabText(3, 'Будущее')
        self.tabWidget.setTabText(4, 'Выбор')
        self.tabWidget.setTabText(5, 'Угадай чиcло')
        self.n1, self.n2 = 'от', 'до'
        self.diap.clicked.connect(self.run1)
        self.label_1.setText('  ОТ ')
        self.label_2.setText('  ДО ')
        self.pushButton.clicked.connect(self.r)
        self.spinBox.setMaximum(9)
        self.spinBox_2.setMaximum(9)
        self.spinBox_3.setMaximum(9)
        self.spinBox_4.setMaximum(9)
        self.pushButton_6.clicked.connect(self.run6)
        self.pushButton_7.clicked.connect(self.run7)
        self.rules_but.clicked.connect(self.rules)
        self.noun_but.clicked.connect(self.noun)
        self.verb_but.clicked.connect(self.verb)
        self.adj_but.clicked.connect(self.adj)
        self.all_but.clicked.connect(self.alll)
        self.translate_but.clicked.connect(self.translate)
        self.add_but.clicked.connect(self.add)
        self.del_but.clicked.connect(self.delete)
        self.clear_but.clicked.connect(self.clear)
        self.pushButton_2.clicked.connect(self.make_choice)
        self.choice.setStyleSheet(f"background-color: rgb{self.color2}")
        self.pushButton_3.clicked.connect(self.predskaz)
        # self.pushButton_4.clicked.connect(self.sovet)

    def predskaz(self):
        f = open('predskaz.txt', encoding='utf8')
        pred = f.readlines()
        pred = [e.replace('\n', '') for e in pred]
        f.close()
        pred1 = random.choice(pred)
        self.label_5.setStyleSheet(f"background-color: rgb{self.color2}")
        self.label_5.setText(' ' + pred1)

    # def sovet(self):
    #     f = open('sovet.txt', encoding='utf8')
    #     sov = f.readlines()
    #     sov = [e.replace('\n', '') for e in sov]
    #     f.close()
    #     sov1 = random.choice(sov)
    #     self.label_5.setStyleSheet(f"background-color: rgb{self.color2}")
    #     self.label_5.setText(' ' + sov1)

    def make_choice(self):
        global elements
        count, ok_pressed = QInputDialog.getItem(
            self, "Выберите", "Сколько вам нужно выбрать элементов?",
            ('1', '2', '3'), 1, False)
        if ok_pressed:
            try:
                count = int(count)
                if len(elements) == 0:
                    raise EmptyError
                if count == 1:
                    el = random.choice(elements)
                    self.choice.setText('\t' + el)
                if count > len(elements):
                    raise LengError
                elif count == 2:
                    elem = random.choices(elements, k=2)
                    self.choice.setText('  1)' + elem[0] + '\n  2)' + elem[-1])
                elif count == 3:
                    elem = random.choices(elements, k=3)
                    self.choice.setText('  1)' + elem[0] + '\n  2)' + elem[1] + '\n  3)' + elem[-1])
            except EmptyError:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText(f"Вы ещё не добавили ни одного элемента")
                x = msg.exec_()
            except LengError:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText(f"С списке слишком мало элементов")
                x = msg.exec_()

    def add(self):
        global elements
        try:
            if self.element.text() not in elements:
                elements.append(self.element.text())
            else:
                raise NotSameError
        except NotSameError:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText(f"Элементы не должны повторяться")
            x = msg.exec_()

    def delete(self):
        global elements
        try:
            if len(elements) == 0:
                raise EmptyError
            if self.element.text() not in elements:
                raise ElementNotInError
            else:
                elements.remove(self.element.text())
        except ElementNotInError:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText(f"Такого элемента нет в списке")
            x = msg.exec_()
        except EmptyError:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText(f"Вы ещё не добавили ни одного элемента")
            x = msg.exec_()

    def clear(self):
        global elements
        ok, ok_pressed = QInputDialog.getItem(
            self, "Уверены?", "Вы уверены, что хотите очистить список?",
            ("Да", "Нет"), 1, False)
        if ok == "Да" and ok_pressed:
            elements.clear()
            msg = QMessageBox()
            msg.setWindowTitle("Успешно")
            msg.setText(f"Список был успешно очистен")
            x = msg.exec_()

    def run1(self):
        self.n1, ok_pressed1 = QInputDialog.getText(self, "Введите число", "От:")
        self.n2, ok_pressed2 = QInputDialog.getText(self, "Введите число", "До:")
        if ok_pressed1:
            self.label_1.setText('  ОТ ' + self.n1)
            self.label_1.setStyleSheet(
                "background-color: rgb(170, 200, 255)")
        if ok_pressed2:
            self.label_2.setText('  ДО ' + self.n2)
            self.label_2.setStyleSheet(
                "background-color: rgb(170, 200, 255)")

    def r(self):
        try:
            if self.n1 == 'от':
                raise Type6Error
            if not self.n1.isdigit() and self.n2.isdigit():
                raise Type1Error
            if not self.n2.isdigit() and self.n1.isdigit():
                raise Type2Error
            if not self.n1.isdigit() and not self.n2.isdigit():
                raise Type3Error
            if int(self.n1) == int(self.n2):
                raise Type4Error
            if int(self.n1) > int(self.n2):
                raise Type5Error
            n = random.randrange(int(self.n1), int(self.n2) + 1)
            self.label.setText('   ' + str(n))
            self.label.setStyleSheet(
                f"background-color: rgb{self.color2}")
        except Type1Error:
            self.label.setStyleSheet(
                "background-color: rgb(233, 131, 131)")
            self.label.setText(' Поменяйте первый\n элемент на число')
        except Type2Error:
            self.label.setStyleSheet(
                "background-color: rgb(233, 131, 131)")
            self.label.setText(' Поменяйте второй\n элемент на число')
        except Type3Error:
            self.label.setStyleSheet(
                "background-color: rgb(233, 131, 131)")
            self.label.setText(' Смените элементы \nдиапазона на числа')
        except Type4Error:
            self.label.setStyleSheet(
                "background-color: rgb(233, 131, 131)")
            self.label.setText(' Числа диапазона не\nдолжны быть равны')
        except Type5Error:
            self.label.setStyleSheet(
                "background-color: rgb(233, 131, 131)")
            self.label.setText('Второе число должно\nбыть больше первого')
        except Type6Error:
            self.label.setStyleSheet(
                "background-color: rgb(233, 131, 131)")
            self.label.setText('      Введите числа\n        диапазона')
        except Exception:
            self.label.setStyleSheet(
                "background-color: rgb(233, 131, 131)")
            self.label.setText('       Поменяйте числа\n    диапазона')

    def run6(self):
        global name
        global n
        fun, ok_pressed = QInputDialog.getItem(
            self, "Выберите", "Что вы хотите сделать?",
            ("Начать игру", "Сбросить текущую игру"), 1, False)
        if ok_pressed and fun == "Начать игру":
            name, ok_pressed = QInputDialog.getText(
                self, "Впишите", "Как Вас зовут?", False)
            while name == '':
                name, ok_pressed = QInputDialog.getText(
                    self, "Впишите", "Как Вас зовут?", False)
            n = random.randrange(1000, 9999)
        if ok_pressed and fun == "Сбросить текущую игру":
            n = 0
        print(n)

    def run7(self):
        global k
        global write
        global n
        ans1 = str(self.spinBox.value())
        ans2 = str(self.spinBox_2.value())
        ans3 = str(self.spinBox_3.value())
        ans4 = str(self.spinBox_4.value())
        ans = int(ans1 + ans2 + ans3 + ans4)
        print(n, ans)
        try:
            if n == 0:
                raise Exception
            if n == ans:
                correct = True
            if n > ans:
                correct = False
                write = 'Загаданное число >'
            if n < ans:
                correct = False
                write = 'Загаданное число <'
            if correct:
                msg = QMessageBox()
                msg.setWindowTitle("Результат")
                print("insert000")
                msg.setText(f"Вы победили! Количество попыток: {k}")
                x = msg.exec_()
                con = sqlite3.connect(self.bd_name)
                cur = con.cursor()
                cur.execute(f'''INSERT INTO itog(name) VALUES("{name}")''')
                print("insert")
                cur.execute(f'''INSERT INTO itog(cout) VALUES("{k}")''')
                con.commit()
                con.close()
                n = 0
                k = 0
            else:
                k += 1
                if write == 'Загаданное число >':
                    msg = QMessageBox()
                    msg.setWindowTitle("Результат")
                    msg.setText(f"Попробуйте ещё раз! Загаданное число > вашего числа")
                    x = msg.exec_()
                if write == 'Загаданное число <':
                    msg = QMessageBox()
                    msg.setWindowTitle("Результат")
                    msg.setText(f"Попробуйте ещё раз! Загаданное число < вашего числа")
                    x = msg.exec_()
        except Exception as e:
            print(e)
            msg = QMessageBox()
            msg.setWindowTitle("Результат")
            msg.setText(f"Ошибка! Возможно вы не начали игру")
            x = msg.exec_()

    def rules(self):
        msg = QMessageBox()
        msg.setWindowTitle("Правила")
        msg.setText(f"Загадано четырёхзначное число.\n Ваша задача угадать число. Вaм будут даны подсказки '>' '<'")
        x = msg.exec_()

    # def lang(self):
    #     global language
    #     global translator1
    #     global translator2
    #     lang, ok_pressed = QInputDialog.getItem(self, "Выберите язык", "Какой язык вас интересует?",
    #                                             ("Русский", "Английский"), 1,
    #                                             False)
    #     que, ok_pressed_2 = QInputDialog.getItem(self, "Выберите", "Перевести всю страницу?",
    #                                              ("Да", "Нет"), 1,
    #                                              False)
    #     if ok_pressed:
    #         if lang == "Русский":
    #             language = ''
    #             self.translate_but.setEnabled(False)
    #         if lang == "Английский":
    #             language = translator1
    #             self.translate_but.setEnabled(True)
    #     if ok_pressed_2 and ok_pressed:
    #         if que == "Да":
    #             if lang == "Русский":
    #                 self.noun_but.setText("Существительное")
    #                 self.verb_but.setText("Глагол")
    #                 self.adj_but.setText("Прилагательное")
    #                 self.all_but.setText("Все")
    #                 self.translate_but.setText("Перевести")
    #                 self.lang_but.setText("Выбрать язык")
    #             if lang == "Английский":
    #                 self.noun_but.setText("Noun")
    #                 self.verb_but.setText("Verb")
    #                 self.adj_but.setText("Adjective")
    #                 self.all_but.setText("All")
    #                 self.translate_but.setText("Translate")
    #                 self.lang_but.setText("Choose language")

    def noun(self):
        global noun
        global s
        s = random.choice(noun)
        s1 = s
        self.label_3.setText('  ' + s1.lower())
        self.label_4.setText('')

    def verb(self):
        global verb
        global s
        s = random.choice(verb)
        s1 = s
        self.label_3.setText('  ' + s1.lower())
        self.label_4.setText('')

    def adj(self):
        global adj
        global s
        global language
        s = random.choice(adj)
        s1 = s
        self.label_3.setText('  ' + s1.lower())
        self.label_4.setText('')

    def alll(self):
        global alll
        global s
        global language
        s = random.choice(alll)
        s1 = s
        self.label_3.setText('  ' + s1.lower())
        self.label_4.setText('')

    def translate(self):
        global s
        self.label_4.setText('  ' + s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Notebook2()
    ex.show()
    sys.exit(app.exec_())
