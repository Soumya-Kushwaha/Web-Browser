import sys
# This command will import the sys module. The sys module contains methods and 
# variables for modifying many aspects of the Python runtime environment. 
# The python interpreter provides access to a number of variables, constants, functions, and methods.

from PyQt5.QtCore import *

from PyQt5.QtWidgets import *
# Qtwidgets are used to generate the user interface in Qt. 
# and it also includes classes for constructing traditional desktop-style 
# user interfaces but these widgets are more useful when developing large-scale applications.

from PyQt5.QtWebEngineWidgets import *
# The QtWebEngineWidgets package contains both a web browser engine and C++ classes for rendering 
# and interacting with web content. The web content is embedded in the application using this framework.

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

# QMainWindow(): The user interface of an application is built using a primary window. 
# QMainWindow and its related classes in Qt are used to handle the main window. 
# QToolBars, QDockWidgets, a QMenuBar, and a QStatusBar can all be added to QMainWindow’s layout.

# QWebEngineView(): The QWebEngineView class implements a widget for viewing and editing web pages. 
# The core widget component of the Qt WebEngine web browsing module is a web view. 
# It can be used to display live online material from the Internet in various different applications.

# setUrl(): This is used to set the default URL of our choice.
# setCentralWidget(): For our applications we can also use custom widgets.
# setCentralWidget() is used to set the central widget.
# showMaximized(): This helps to set the window size to maximum.
# QToolBar(): This will add a toolbar and can be set to movable, immovable using setMovable(), isMovable() etc.

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Copy Assignments Browser')
window = MainWindow()
app.exec_()