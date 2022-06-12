# region[2022-01-29]

# function
# def call():
#     print('call!!!!')
#     print('call!!!!')
#     print('call!!!!')
#
# call()
#
# def call_sum(a, b):
#     return a + b
#
# d = call_sum(3, 4)
# print(d)
#
#
#
# def call_multi(a, b):
#     return a * b
#
# e = call_multi(3, 4)
# print(e)
#

# class
# class Cat:
#     color = 'black'
#     age = 1
#
#     def meow(self):
#         print('meow meow')
#
#     def crow(self):
#         print('crow')
#
# cat = Cat()
# cat2 = Cat()
#
# print(cat.color)
# print(cat.age)
# cat.meow()
# cat.crow()
#
# cat.color = 'white'
# print(cat.color)
# print(cat2.color)
# endregion

# region [2022-01-15]

# print('こんにちは')
#
# print(1+7)
#
# print('こんに'+'ちは')
#
# print('こんに'+str(1))
#
# a=3
# b=2
# c=a+b
# print(a)
# print(type(c))
# d=1.5
# print(type(d))
#
# # region [tuple]
# # t1=(1, 2)
# # print(t1)
# #
# # t2=('a', 'b')
# # print(t2)
# #
# # t3=(t1, t2)
# # print(t3)
# # endregion
#
# test=[1,2,3,4]
# del test[0]
# print(test)
#
# test.reverse()
# print(test)
#
# test=[1,3,4,2]
# test.sort()
# print(test)
#
# dic={1: 'Hi', 2: 'My', 3:'name', 4:'is'}
# print(dic[3])
# print(dic.keys())
# print(dic.values())
# print(dic.items())

# endregion

# region [2022-01-15]
# for i in range(100):
#     print(i)
#
# menulist=['キムチ', 'サムギョプサル', 'こぷちゃん']
#
# for menu in menulist:
#     print(menu)

# #反復法
# for i in range(2, 10):
#     for j in range(1, 10):
#         print('{}*{}={}'.format(i, j, i*j))

#条件分
# a =8
# if a >= 10:
#     print('aの値は10です')
# else:
#     print('aの値は10より小さいです')
#
# b = 100
#
# if b > 100:
#     print('bの値は100より大きいです')
# elif b == 100:
#     print('bの値は100と同じです')
# else:
#     print('bの値は100より小さいです')
#


# a = 0
# while a < 10:
#     print('h1')
#     a = a+1

# count = 0
# while True:
#     print('あぁ')
#     count = count + 1
#
#     if count == 10:
#         print('脱出だ')
#         break
#
# print('end!!!')

# print('こんにちは')
#
# print(1+7)
#
# print('こんに'+'ちは')
#
# print('こんに'+str(1))
#
# a=3
# b=2
# c=a+b
# print(a)
# print(type(c))
# d=1.5
# print(type(d))
#
# # region [tuple]
# # t1=(1, 2)
# # print(t1)
# #
# # t2=('a', 'b')
# # print(t2)
# #
# # t3=(t1, t2)
# # print(t3)
# # endregion
#
# test=[1,2,3,4]
# del test[0]
# print(test)
#
# test.reverse()
# print(test)
#
# test=[1,3,4,2]
# test.sort()
# print(test)
#
# dic={1: 'Hi', 2: 'My', 3:'name', 4:'is'}
# print(dic[3])
# print(dic.keys())
# print(dic.values())
# print(dic.items())

# endregion

# region [2022-01-15]

# print('こんにちは')
#
# print(1+7)
#
# print('こんに'+'ちは')
#
# print('こんに'+str(1))
#
# a=3
# b=2
# c=a+b
# print(a)
# print(type(c))
# d=1.5
# print(type(d))
#
# # region [tuple]
# # t1=(1, 2)
# # print(t1)
# #
# # t2=('a', 'b')
# # print(t2)
# #
# # t3=(t1, t2)
# # print(t3)
# # endregion
#
# test=[1,2,3,4]
# del test[0]
# print(test)
#
# test.reverse()
# print(test)
#
# test=[1,3,4,2]
# test.sort()
# print(test)
#
# dic={1: 'Hi', 2: 'My', 3:'name', 4:'is'}
# print(dic[3])
# print(dic.keys())
# print(dic.values())
# print(dic.items())

# endregion

#region[2022-02-20]
# import csv
#
# csv_path = 'data.csv'
# f = open(csv_path, 'r', encoding='cp949')
# data = csv.reader(f, delimiter=',')
#
# first_row = next(data)
#
# max_date = ''
# max_temp = -100
#
# for row in data:
#     if row[4] == '':
#         row[4] = -100
#
#     row[4] = float(row[4])
#
#     if max_temp < row[4]:
#         max_temp = row[4]
#         max_date = row[0]
#
# f.close()
#
# print('最高気温:{}度, 日付:{}'.format(max_temp, max_date))
#
# # 宿題：
# # 最低気温を出すこと！
#
# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4, 5]
# y = [1, 2, 3, 4, 5]
# y_2 =[4, 5, 6, 3, 2]
#
# plt.title('test')
# plt.plot(x, y, ls='--', color='red', label='y')
# plt.plot(x, y_2, ls=':', color='blue', label='y_2')
# plt.legend()
# plt.show()
# endregion

# region[2022-05-15][2022-05-29]
#import sys
#from PyQt5 import uic
#from PyQt5.QtWidgets import QApplication, QMainWindow

#form_class = uic.loadUiType("C:/Users/inoue/OneDrive/デスクトップ/python_gui/My_UI.ui")[0]

#class WindowClass(QMainWindow, form_class):
#   def __init__(self):
#       super().__init__()
#       self.setupUi(self)

#       self.enableFlag1 = False
#       self.enableFlag2 = False
#       self.enableFlag3 = False
#       self.enableFlag4 = False

#       self.pushButton_OK.clicked.connect(self.btnClick_OK)

#       self.lineEdit_Email.textChanged.connect(self.test1)
#       self.lineEdit_Username.textChanged.connect(self.test2)
#       self.lineEdit_Password1.textChanged.connect(self.test3)
#       self.lineEdit_Password2.textChanged.connect(self.test4)

#   def test1(self):
#       print("文字が変わりました1")
#       if self.lineEdit_Email.text() != "":
#           self.enableFlag1 = True
#       else:
#            self.enableFlag1 = False

#       if self.enableFlag1 == True and self.enableFlag2 == True and self.enableFlag3 == True and self.enableFlag4 == True:
#           self.pushButton_OK.setEnabled(True)
#       else:
#            self.pushButton_OK.setDisabled(True)
#    def test2(self):
#        print("文字が変わりました2")
#       if self.lineEdit_Username.text() != "":
#            self.enableFlag2 = True
#        else:
#            self.enableFlag2 = False

#        if self.enableFlag1 == True and self.enableFlag2 == True and self.enableFlag3 == True and self.enableFlag4 == True:
#            self.pushButton_OK.setEnabled(True)
#        else:
#            self.pushButton_OK.setEnabled(False)
#    def test3(self):
#         print("文字が変わりました3")
#         if self.lineEdit_Password1.text() != "":
#             self.enableFlag3 = True
#         else:
#             self.enableFlag3 = False
#
#         if self.enableFlag1 == True and self.enableFlag2 == True and self.enableFlag3 == True and self.enableFlag4 == True:
#             self.pushButton_OK.setEnabled(True)
#         else:
#             self.pushButton_OK.setEnabled(False)
# #    def test4(self):
#         print("文字が変わりました4")
#         if self.lineEdit_Password2.text() != "":
#             self.enableFlag4 = True
#         else:
#             self.enableFlag4 = False
#
#         if self.enableFlag1 == True and self.enableFlag2 == True and self.enableFlag3 == True and self.enableFlag4 == True:
#             self.pushButton_OK.setEnabled(True)
#         else:
#             self.pushButton_OK.setEnabled(False)

#   def btnClick_OK(self):
#        print("버튼이 클릭되었습니다.")

#       email = self.lineEdit_Email.text()
#       username = self.lineEdit_Username.text()
#       password1 = self.lineEdit_Password1.text()
#       password2 = self.lineEdit_Password2.text()

#       result = f"email=> {email}, username=> {username}, password1=> {password1}, password2=> {password2}"
#       print(result)

#       if email is not "" and username is not "" and password1 is not "" and password2 is not "":
#            print("全部入力完了しました")
#        else:
#             print("確認してください")
#             self.label_result.setStyleSheet("Color : red")
#             self.label_result.setText("確認してください")
#             return
#
#         if len(password1) >= 8 and len(password1) <= 20:
#             if password1 == password2:
#                 print("パスワードが一致しました")
#                 self.label_result.setStyleSheet("Color : black")
#                 self.label_result.setText("パスワードが一致しました")
#             else:
#                 print("パスワードが間違っています")
#                 self.label_result.setStyleSheet("Color : red")
#                 self.label_result.setText("パスワードが間違っています")
#         else:
#             print("パスワードの長さを確認してください")
#             self.label_result.setStyleSheet("Color : red")
#             self.label_result.setText("パスワードの長さを確認してください")
#             return



# #if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myWindow = WindowClass()
#     myWindow.show()
#     app.exec_()

# endregion