from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtWidgets, QtCore
from googletrans import *
from transliterate import *
import PyQt5
from PyQt5 import QtWidgets, uic, QtGui
import sys
from my import Ui_MainWindow
import sys


def text_translate(text, src="ru", dest="en"):
    if text == "":
        return ""
    translator = Translator()
    translator = translator.translate(text=text, src=src, dest=dest)
    return translator.text


def text_translit(text):
    dic = {'Ь': '', 'ь': '', 'Ъ': '', 'ъ': '', 'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v',
           'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e', 'Ё': 'E', 'ё': 'e', 'Ж': 'Zh', 'ж': 'zh',
           'З': 'Z', 'з': 'z', 'И': 'I', 'и': 'i', 'Й': 'I', 'й': 'i', 'К': 'K', 'к': 'k', 'Л': 'L', 'л': 'l',
           'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r',
           'С': 'S', 'с': 's', 'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u', 'Ф': 'F', 'ф': 'f', 'Х': 'Kh', 'х': 'kh',
           'Ц': 'Tc', 'ц': 'tc', 'Ч': 'Ch', 'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh', 'Щ': 'Shch', 'щ': 'shch', 'Ы': 'Y',
           'ы': 'y', 'Э': 'E', 'э': 'e', 'Ю': 'Iu', 'ю': 'iu', 'Я': 'Ia', 'я': 'ia'}

    alphabet = ['Ь', 'ь', 'Ъ', 'ъ', 'А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё',
                'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о',
                'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х', 'Ц', 'ц', 'Ч', 'ч',
                'Ш', 'ш', 'Щ', 'щ', 'Ы', 'ы', 'Э', 'э', 'Ю', 'ю', 'Я', 'я']

    len_st = len(text)
    simb = ""
    result = ""
    for i in range(0, len_st):
        if text[i] in alphabet:
            simb = dic[text[i]]
        else:
            simb = text[i]
        result = result + simb
    return result


def gen1(names, text):
    s = ""
    for i in range(len(names)):
        if i == len(names) - 1:
            s = s + text_translit(names[i]) + " "
        else:
            s = s + text_translit(names[i]) + ", "
    s = s + text_translit(text) + " [" + text_translate(text) + "]"
    return s


def clear_text(text):
    text_part = []
    for i in range(len(text)):
        s = ""
        for j in range(len(text[i])):
            if text[i][j] != '.' and text[i][j] != ',':
                s += text[i][j]
        text_part.append(s)
    return text_part


def translit_format(text):
    if text == "":
        return ""
    # print(text_translate(text))
    # print(text_translit(text))
    text = text.split()
    text_1 = []
    first_part = ""
    for i in range(len(text)):
        if text[i] == "/":
            break
        text_1.append(text[i])
    text_part_1 = clear_text(text_1)
    # print(text)
    # print(text_part_1)
    name_part_1 = []
    s_base = ""
    for i in range(1, len(text_part_1)):
        s = ""
        if text_part_1[i].isupper() and len(text_part_1[i - 1]) > 1:
            s = text_part_1[i - 1] + " " + text_part_1[i] + "."
            for j in range(i + 1, len(text_part_1)):
                if text_part_1[j].isupper():
                    s = s + text_part_1[j] + "."
                else:
                    break
            name_part_1.append(s)
        else:
            s_base = s_base + text_part_1[i] + " "
    s_base = s_base.strip()
    # print(name_part_1)

    text_part_2_old = []
    s = ""
    flag = False
    other_autor = False
    for i in range(len(text)):
        if text[i] == '[и':
            flag = False
            other_autor = True
        if text[i] == '//':
            flag = False
            break
        if flag:
            s += text[i]
        if text[i] == '/':
            flag = True
    text_part_2_old = s.split(",")
    text_part_2_new = []
    # print(text_part_2_old)
    for i in range(len(text_part_2_old)):
        text_part_2_new.append(text_part_2_old[i].split("."))
    # print(text_part_2_new)
    for i in range(len(text_part_2_new)):
        text_part_2_new[i].insert(0, text_part_2_new[i][-1])
        del text_part_2_new[i][-1]
    # print(text_part_2_new)
    text_part_2 = []
    for i in range(len(text_part_2_new)):
        s = ""
        for j in range(len(text_part_2_new[i])):
            if j == 0:
                s = s + text_part_2_new[i][j] + " "
            else:
                s = s + text_part_2_new[i][j] + "."
        text_part_2.append(s)
    # print(text_part_2)
    text_name = []
    for i in range(len(name_part_1)):
        text_part_2.append(name_part_1[i])
    # print(text_part_2)
    # text_name = list(set(text_part_2))
    # text_name = text_part_2
    text_name = []
    [text_name.append(x) for x in text_part_2 if x not in text_name]
    # print(text_name)
    # нашли все имена
    if len(s_base) > 1:
        if s_base[0].isupper():
            s_base = s_base.replace(s_base[0], "")
        s_base = s_base.strip()
        s_base = s_base[0].upper() + s_base[1:]
        first_part = gen1(text_name, s_base) + '.'
    # print(text)
    name_book = ""
    flag = False
    first_dash = 0
    for i in range(len(text)):
        if text[i] == '–':
            flag = False
            first_dash = i
            break
        if flag:
            name_book += text[i] + " "
        if text[i] == '//':
            flag = True
    name_book = name_book[:-2]
    second_part = ""
    for i in range(first_dash + 1, len(text)):
        # print(text[i])
        if ((text[i][-1] == '.' or text[i][-1] == ',') and len(text[i]) > 2) or (
                text[i][-1] == '.' and text[i][:-1] in '0123456789'):
            text[i] = text[i][:-1] + ', '
            second_part += text[i]
        elif text[i][-1] == '.':
            second_part += text[i]
        elif text[i] == '–' and len(text[i]) == 1:
            continue
        elif text[i] == 'EDN':
            break
        elif text[i] == "DOI":
            second_part += text[i] + ": "
        else:
            second_part += text[i]
    second_part = second_part[:-2]
    second_part = second_part.replace("Т.", "V.")
    second_part = second_part.replace("№", "I.")
    second_part = second_part.replace("С.", "pp.")
    second_part = text_translit(name_book) + " [" + text_translate(name_book) + "]. " + second_part + ". (in Russian)"
    if other_autor:
        return "!!!Необходимо проверить количество авторов!!! " + "\n" + first_part + "// " + second_part
    return first_part + " " + second_part


def original_format(text):
    if text == "":
        return ""
    other_author = False
    flag = True
    ans = ""
    if "[и др.]" in text:
        other_author = True
    for i in range(1, len(text)):
        if text[i] == "[":
            flag = False
        if flag:
            ans += text[i]
        if text[i] == "]":
            flag = True
    ind = ans.rfind("–")
    ans_ret = ""
    for i in range(len(ans)):
        if ind == i:
            break
        ans_ret += ans[i]
    first_author = False
    for i in range(len(text)):
        if text[i] == "/":
            break
        if text[i].isupper() and text[i + 1] == ".":
            first_author = True
            break

    fir_aut = []
    temp = ""

    if not first_author:
        for i in range(len(text)):
            if text[i] == "/":
                for j in range(i + 1, len(text)):
                    if text[j] == ",":
                        break
                    if text[j] == " ":
                        fir_aut.append(temp)
                        temp = ""
                    temp += text[j]
                fir_aut.append(temp.strip())
                break
    ind = ans_ret.find("/")
    temp = ""
    ans_ret = ans_ret[:ind] + "[Текст] " + ans_ret[ind:]
    if not first_author:
        for i in range(len(fir_aut)):
            temp += (fir_aut[len(fir_aut) - 1 - i])
    else:
        ans_ret = ans_ret.replace(",", "", 1)
    if other_author:
        return "!!!Необходимо проверить количество авторов!!! " + "\n" + (temp + " " + ans_ret).strip()
    return (temp + " " + ans_ret).strip()


def original_translit(text):
    if text == "":
        return ""
    text = text.replace("[Текст]", "")
    # print(text_translate(text))
    # print(text_translit(text))
    text = text.split()
    text_1 = []
    first_part = ""
    for i in range(len(text)):
        if text[i] == "/":
            break
        text_1.append(text[i])
    text_part_1 = clear_text(text_1)
    # print(text)
    # print(text_part_1)
    name_part_1 = []
    s_base = ""
    for i in range(1, len(text_part_1)):
        s = ""
        if text_part_1[i].isupper() and len(text_part_1[i - 1]) > 1:
            s = text_part_1[i - 1] + " " + text_part_1[i] + "."
            for j in range(i + 1, len(text_part_1)):
                if text_part_1[j].isupper():
                    s = s + text_part_1[j] + "."
                else:
                    break
            name_part_1.append(s)
        else:
            s_base = s_base + text_part_1[i] + " "
    s_base = s_base.strip()
    for i in range(len(name_part_1)):
        for j in range(i + 1, len(name_part_1[i])):
            if name_part_1[i][j].isupper() and not name_part_1[i][j + 1].isupper():
                name_part_1[i] = name_part_1[i][:j] + "." +name_part_1[i][j:]
        name_part_1[i] = name_part_1[i].replace("..", ".")
    s = ""
    flag = False
    other_autor = False
    for i in range(len(text)):
        if text[i] == '[и':
            flag = False
            other_autor = True
        if text[i] == '//':
            flag = False
            break
        if flag:
            s += text[i]
        if text[i] == '/':
            flag = True
    text_part_2_old = s.split(",")
    text_part_2_new = []
    # print(text_part_2_old)
    for i in range(len(text_part_2_old)):
        text_part_2_new.append(text_part_2_old[i].split("."))
    # print(text_part_2_new)
    for i in range(len(text_part_2_new)):
        text_part_2_new[i].insert(0, text_part_2_new[i][-1])
        del text_part_2_new[i][-1]
    # print(text_part_2_new)
    text_part_2 = []
    for i in range(len(text_part_2_new)):
        s = ""
        for j in range(len(text_part_2_new[i])):
            if j == 0:
                s = s + text_part_2_new[i][j] + " "
            else:
                s = s + text_part_2_new[i][j] + "."
        text_part_2.append(s)
    # print(text_part_2)
    text_name = []
    for i in range(len(name_part_1)):
        text_part_2.append(name_part_1[i])
    text_name = []
    [text_name.append(x) for x in text_part_2 if x not in text_name]
    # нашли все имена
    if len(s_base) > 1:
        #if s_base[0].isupper():
            #s_base = s_base.replace(s_base[0], "")
        s_base = s_base.strip()
        s_base = s_base[0].upper() + s_base[1:]
        first_part = gen1(text_name, s_base) + '.'
    # print(text)
    name_book = ""
    flag = False
    first_dash = 0
    for i in range(len(text)):
        if text[i] == '–':
            flag = False
            first_dash = i
            break
        if flag:
            name_book += text[i] + " "
        if text[i] == '//':
            flag = True
    name_book = name_book[:-2]
    second_part = ""
    for i in range(first_dash + 1, len(text)):
        # print(text[i])
        if ((text[i][-1] == '.' or text[i][-1] == ',') and len(text[i]) > 2) or (
                text[i][-1] == '.' and text[i][:-1] in '0123456789'):
            text[i] = text[i][:-1] + ', '
            second_part += text[i]
        elif text[i][-1] == '.':
            second_part += text[i]
        elif text[i] == '–' and len(text[i]) == 1:
            continue
        elif text[i] == 'EDN':
            break
        elif text[i] == "DOI":
            second_part += text[i] + ": "
        else:
            second_part += text[i]
    second_part = second_part[:-2]
    second_part = second_part.replace("Т.", "V.")
    second_part = second_part.replace("№", "I.")
    second_part = second_part.replace("С.", "pp.")
    second_part = text_translit(name_book) + " [" + text_translate(name_book) + "]. " + second_part + ". (in Russian)"
    if other_autor:
        return "!!!Необходимо проверить количество авторов!!! " + "\n" + first_part + "// " + second_part
    return first_part + " " + second_part


# text = input()
# print(translit_format(text))

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textEdit_2.setReadOnly(True)
        self.ui.pushButton.clicked.connect(self.Translate)
        self.ui.pushButton_2.clicked.connect(self.Translit)
        self.ui.pushButton_3.clicked.connect(self.ORG)
        self.ui.pushButton_4.clicked.connect(self.RINZ)
        self.ui.pushButton_5.clicked.connect(self.copy)
        self.ui.pushButton_6.clicked.connect(self.ORINZ)

    def Translate(self):
        text = self.ui.textEdit.toPlainText()
        self.ui.textEdit_2.setText(text_translate(text))

    def Translit(self):
        text = self.ui.textEdit.toPlainText()
        self.ui.textEdit_2.setText(text_translit(text))

    def RINZ(self):
        text = self.ui.textEdit.toPlainText()
        self.ui.textEdit_2.setText(translit_format(text))

    def copy(self):
        text = self.ui.textEdit_2.toPlainText()
        self.clip = QtWidgets.QApplication.clipboard()
        self.clip.setText(text)

    def ORG(self):
        text = self.ui.textEdit.toPlainText()
        self.ui.textEdit_2.setText(original_format(text))

    def ORINZ(self):
        text = self.ui.textEdit.toPlainText()
        self.ui.textEdit_2.setText(original_translit(text))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())
