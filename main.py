from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Web Browser")

        # Create a QWebEngineView widget
        self.view = QWebEngineView(self)

        # Create a QVBoxLayout
        layout = QVBoxLayout()

        # Add the view to the layout
        layout.addWidget(self.view)

        # Set the layout
        self.setLayout(layout)

        # Load a website
        self.view.load(QUrl("https://www.google.com"))

        self.show()

if __name__ == "__main__":
    app = QApplication([])
    browser = Browser()
    app.exec_()
