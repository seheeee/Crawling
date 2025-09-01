<<<<<<< HEAD
import sys
from PySide6.QtWidgets import QApplication, QWidget #QApplication(기본객체 클래스), QWidget(기본 창 클래스)
from login_ui import Ui_Form

class MainWindow(QWidget, Ui_Form): #두 개 클래스를 "상속" 받음
    def __init__(self):
        super().__init__() #부모클래스(QWidget)의 생성자를 호출
        self.setupUi(self) #Ui_Form의 setupUi을 호출

        #self.객체이름.clicked.connect(self.실행할 매서드 이름)
        self.login_btn.clicked.connect(self.login) #버튼 로그인하면 login함수로 연결

    def login(self):
        print(f'아이디 :{self.id.text()} 비밀번호 : {self.pw.text()}')
        
app = QApplication() #객체 생성

window = MainWindow() #창 객체 생성
window.show()

# sys.exit(app.exec()) #프로그램 계속 실행
=======
import sys
from PySide6.QtWidgets import QApplication, QWidget #QApplication(기본객체 클래스), QWidget(기본 창 클래스)
from login_ui import Ui_Form

class MainWindow(QWidget, Ui_Form): #두 개 클래스를 "상속" 받음
    def __init__(self):
        super().__init__() #부모클래스(QWidget)의 생성자를 호출
        self.setupUi(self) #Ui_Form의 setupUi을 호출

        #self.객체이름.clicked.connect(self.실행할 매서드 이름)
        self.login_btn.clicked.connect(self.login) #버튼 로그인하면 login함수로 연결

    def login(self):
        print(f'아이디 :{self.id.text()} 비밀번호 : {self.pw.text()}')
        
app = QApplication() #객체 생성

window = MainWindow() #창 객체 생성
window.show()

sys.exit(app.exec()) #프로그램 계속 실행
>>>>>>> ec2bb7fffdb101638cbff32c98cb6a641f604ba6
