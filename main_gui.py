# region[2022-06-04]
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("python_gui/My_UI2.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.enableFlag1 = False
        self.enableFlag2 = False

        self.pushButton.clicked.connect(self.btnClick_OK)

        self.lineEdit_email.textChanged.connect(self.test1)
        self.lineEdit_name.textChanged.connect(self.test2)

    def test1(self):
        print("emailが入力されました")

        if self.lineEdit_email.text() != "":
            self.enableFlag1 = True
        else:
            self.enableFlag1 = False

            if self.enableFlag1 == True and self.enableFlag2 == True:
                self.pushButton.setEnabled(True)
            else:
                self.pushButton.setDisabled(True)

    def test2(self):
        print("ユーザ名が入力されました")
        if self.lineEdit_name.text() != "":
            self.enableFlag2 = True
        else:
            self.enableFlag2 = False



    def btnClick_OK(self):
        print("次へ進むボタンが入力されました")

        email = self.lineEdit_email.text()
        username = self.lineEdit_name.text()
        result = f"email=> {email}, name=> {username}"
        print(result)


        if email is not "" and username is not "":
            print("全て入力完了しました")
        else:
            print("確認してください")
            # self.label_result.setStyleSheet("Color : red")
            # self.label_result.setText("確認してください")
            return

        if len(username) >= 5 and len(username) <= 10:
            print("？？？")
            print("？？？")
            print("？？？")
            print("？？？")
        else:
            print("ユーザ名の長さを確認してください")
            # self.label_result.setStyleSheet("Color : red")
            # self.label_result.setText("パスワードの長さを確認してください")
            return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

# endregion