from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLineEdit

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Web Browser")

        # Create a QWebEngineView widget
        self.view = QWebEngineView(self)

        # Create a QLineEdit for the URL bar
        self.url_bar = QLineEdit(self)
        self.url_bar.setPlaceholderText("https://")

        self.url_bar.returnPressed.connect(self.load_url)

        # Create a QVBoxLayout
        layout = QVBoxLayout()

        # Add the view and the URL bar to the layout
        layout.addWidget(self.view)
        layout.addWidget(self.url_bar)

        # Set the layout
        self.setLayout(layout)

        # Load a website
        self.view.load(QUrl("https://www.google.com"))

        self.show()

    def load_url(self):
        """Load the URL entered in the URL bar"""
        url = self.url_bar.text()
        self.view.load(QUrl(url))

if __name__ == "__main__":
    app = QApplication([])
    browser = Browser()
    app.exec_()
