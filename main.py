import sys
import threading
from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QLocale ,QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent, QBuffer, QByteArray)
from PySide2.QtGui import (QBrush, QMovie, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon,
                           QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_main_window import Ui_MainWindow

# Fake FB user
fb_user = 'alexahuri360@hotmail.com'
fb_password = '3fy9fcnZ$'

## Disable Notifications
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--headless")
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('--disable-gpu')

dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}

authors = []
profiles = []
comments = []
tags = []

def restart():
    MainWindow.singleton = MainWindow()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('britney_ico.ico'))

        # self.email = 'eyal_360@hotmail.com'  # enter your email
        # self.pswrd = '$3fy9fcnZ$'  # enter password

        # Loading the GIF
        self.movie = QMovie("loader.gif")
        self.ui.loader_lbl.setMovie(self.movie)
        self.ui.loader_lbl.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.movie.start()

        self.ui.start_btn.clicked.connect(self.check_inputs)
        self.ui.restart_btn.clicked.connect(self.restart)

    def restart(self):
        self.close()
        restart()

    def export_data(self):
        df = pd.DataFrame({"tag": tags,
                           "author": authors,
                           "profile": profiles,
                           "comment": comments,
                           })

        df.drop_duplicates(subset="comment", keep="first", inplace=True)
        file_name = 'BritneyComments.csv'
        df.to_csv(file_name, encoding='utf-8-sig')
        self.ui.information_lbl.setText(f'קובץ התגובות - {file_name.replace(".csv","")} - נוצר בתיקייה')

    def scrap_comms(self, browser):
        ## AUTHORS
        reply_author = browser.find_elements_by_xpath("//div[@class='_2b05']/a")
        for details in reply_author:
            author = details.text
            profile = details.get_attribute('href')

            authors.append(author)
            profiles.append(profile)
            tags.append('')

        # TEXTS
        tagged_names = []
        names = browser.find_elements_by_xpath("//div[@class='_5wnf']/a")
        for name in names:
            tagged_names.append(name.get_attribute('text'))

        comms = browser.find_elements(By.CLASS_NAME, "_14v5")
        for com in comms:
            comment = com.text
            for name in tagged_names:
                if name in comment:
                    comment = comment.replace(name, '')
            for name in authors:
                if name in comment:
                    comment = comment.replace(name, '')

            comments.append(comment.replace('\n', ''))

    def scrap_replies(self, browser):
        '''
        :param input - driver (usually "browser")
        :return: output -  all of the replies on the current page and already sort them inside the global lists
         (by looking for the original comment and inserting all of them before it).
        '''

        reply_links = []
        raw_replies_links = browser.find_elements_by_xpath("//div[@class='_2b1h async_elem']/a")
        print(f'len raw links = {len(raw_replies_links)}')
        for val in raw_replies_links:
            reply_links.append(val.get_attribute("href"))

        print(f'len links = {len(reply_links)}')

        for link in reply_links:
            print(link)
            reply_authors = []
            reply_profiles = []
            reply_texts = []
            reply_tags = []

            browser.get(link)
            sleep(4)

            # get all authors and comments
            replies = browser.find_elements_by_xpath("//div[@class='_2b05']/a")

            for reply in replies:
                reply_author = reply.text
                reply_profile = reply.get_attribute('href')

                reply_authors.append(reply_author)
                reply_profiles.append(reply_profile)
                reply_tags.append('תגובה')

            # TEXTS
            tagged_names = []
            names = browser.find_elements_by_xpath("//div[@class='_5wnf']/a")
            for name in names:
                tagged_names.append(name.get_attribute('text'))

            comms = browser.find_elements(By.CLASS_NAME, "_14v5")
            for com in comms:
                comment = com.text
                for name in tagged_names:
                    if name in comment:
                        comment = comment.replace(name, '')
                for name in reply_authors:
                    if name in comment:
                        comment = comment.replace(name, '')

                reply_texts.append(comment.replace('\n', ''))

            comment_author = reply_authors[0]
            del reply_authors[0]
            del reply_profiles[0]
            del reply_texts[0]
            del reply_tags[0]

            index = authors.index(comment_author) + 1
            authors[index:index] = reply_authors
            profiles[index:index] = reply_profiles
            comments[index:index] = reply_texts
            tags[index:index] = reply_tags

    def next_page(self, browser):
        '''
        :param insert driver (usually "browser")
        :return: next page link and True/False if its the last page
        '''
        next_page = browser.find_elements_by_xpath("//div[@class='async_elem']/a")
        if len(next_page) == 0:
            next_page_link = ''
        elif len(next_page) == 1:
            next_page_link = next_page[0].get_attribute("href")
        else:
            next_page_link = next_page[1].get_attribute("href")

        return next_page_link

    def how_much_time(self, browser, current_post_page):
        num_of_pages = 0
        num_of_replies_pages = 0
        next_page_link = current_post_page

        ## checking how many PAGES and REPLY PAGES are there
        while next_page_link != '':
            num_of_pages += 1
            next_page = browser.find_elements_by_xpath("//div[@class='async_elem']/a")
            if len(next_page) == 0:
                next_page_link = ''
                try:
                    raw_replies_links = browser.find_elements_by_xpath("//div[@class='_2b1h async_elem']/a")
                    num_of_replies_pages += len(raw_replies_links)
                except:
                    pass
            elif len(next_page) == 1:
                next_page_link = next_page[0].get_attribute("href")
                browser.get(next_page_link)
                try:
                    raw_replies_links = browser.find_elements_by_xpath("//div[@class='_2b1h async_elem']/a")
                    num_of_replies_pages += len(raw_replies_links)
                except:
                    pass
            else:
                next_page_link = next_page[1].get_attribute("href")
                browser.get(next_page_link)
                try:
                    raw_replies_links = browser.find_elements_by_xpath("//div[@class='_2b1h async_elem']/a")
                    num_of_replies_pages += len(raw_replies_links)
                except:
                    pass

        wait_time = (num_of_pages + num_of_replies_pages) * 5 ## we get the calc in seconds
        self.ui.information_lbl.setText(f'סיום בעוד {60/wait_time} דקות')

        browser.get(current_post_page)

    def login(self, browser):
        email_add = browser.find_element_by_id("email")
        email_add.send_keys(self.email)
        password = browser.find_element_by_id("pass")
        password.send_keys(self.pswrd)
        button = browser.find_element_by_name("login")
        button.click()

    def execute_script(self):
        global page

        browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options, desired_capabilities=dc)
        browser.get('https://www.facebook.com')
        sleep(2)

        self.login(browser)
        sleep(4)

        page = 1
        current_post_page = self.link.replace('//www', '//m')
        self.ui.information_lbl.setText(f'מעריך זמנים ...')

        self.how_much_time(browser, current_post_page)

        while current_post_page != '':  # while didnt get to the last page

            browser.get(current_post_page)
            self.ui.information_lbl.setText(f'מושך תגובות מעמוד {page}')
            sleep(5)

            self.scrap_comms(browser)
            sleep(2)

            self.scrap_replies(browser)
            sleep(2)

            browser.get(current_post_page)  # reset all of the links opened

            current_post_page = self.next_page(browser)
            page += 1
            if current_post_page == '':
                self.ui.information_lbl.setText(f'נמשכו בהצלחה {len(authors)} תגובות')

        self.export_data()
        self.ui.loader_lbl.hide()
        browser.quit()  # closing the webdriver

    def check_inputs(self):
        self.link = self.ui.link_text.toPlainText()
        self.email = fb_user
        self.pswrd = fb_password

        if "m." not in self.link and "www." not in self.link:
            self.ui.information_lbl.setText('הלינק אינו תקין, נא להכניס מחדש')
        else:
            self.ui.start_btn.hide()
            self.ui.headline_brit.hide()
            self.ui.link_text.hide()

            self.ui.mid_brit.show()
            self.ui.headline_lbl.setStyleSheet('font: 63 20pt "Segoe UI Semibold";'
                                               'color: rgb(255, 255, 255);')
            self.ui.information_lbl.setText('מפעיל בוט')
            self.ui.loader_lbl.show()
            self.ui.link_text.setText('')
            threading.Thread(target=self.execute_script).start()

    def pop(self):
        self.ui.mid_brit.hide()
        self.ui.loader_lbl.hide()
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.pop()
    sys.exit(app.exec_())