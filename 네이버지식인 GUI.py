import sys
from PySide6.QtWidgets import QApplication, QWidget #QApplication(기본객체 클래스), QWidget(기본 창 클래스)
from naver_kin_ui import Ui_Form

import requests
from bs4 import BeautifulSoup
import pandas as pd

class MainWindow(QWidget, Ui_Form): #두 개 클래스를 "상속" 받음
    def __init__(self):
        super().__init__() #부모클래스(QWidget)의 생성자를 호출
        self.setupUi(self) #Ui_Form의 setupUi을 호출

        #self.객체이름.clicked.connect(self.실행할 매서드 이름)
        self.start_bnt.clicked.connect(self.start)
        self.reset_bnt.clicked.connect(self.reset)
        self.save_bnt.clicked.connect(self.save)
        self.quit_bnt.clicked.connect(self.quit)

    def start(self):
        input_keyword = self.keyword.text()
        input_page = self.page.text()

        self.result =[]
        for i in range(1, int(input_page)+1):
            self.textBrowser.append(f'{i} 페이지 크롤링 중 ...')

            response = requests.get(f"https://kin.naver.com/search/list.naver?query={input_keyword}&page={i}")
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup.select('.basic1 > li') #나무태그 찾기

            for tag in tags:
                title = tag.select_one('._nclicks\\:kin\\.txt').text
                link = tag.select_one('.basic1 a').attrs['href']
                ddate = tag.select_one('.txt_inline').text
                category = tag.select_one('.txt_g1._nclicks\\:kin\\.cat2').text
                answer = tag.select_one('.hit').text.split(' ')[1]
                
                self.textBrowser.append(title)
                QApplication.processEvents() #강제로 ui 업뎃, 한줄씩 나오게 됨

                self.result.append([title, link, ddate, category, answer])
    
        self.textBrowser.append('크롤링 완료!')

    def reset(self):
        self.keyword.setText("")
        self.page.setText("")
        self.textBrowser.setText("")
    
    def save(self):
        input_keyword = self.keyword.text()
        
        df = pd.DataFrame(self.result,columns = ['제목', '링크', '날짜', '카테고리', '답변수'])
        df.to_excel(f'{input_keyword}.xlsx')

    def quit(self):
        sys.exit()

app = QApplication() #객체 생성

window = MainWindow() #창 객체 생성
window.show()

sys.exit(app.exec()) #프로그램 계속 실행