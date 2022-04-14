class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # Resize Windows
        self.resize(500, 500)

        # Create Container
        self.container = QFrame()
        self.container.setObjectName("container")
        self.container.setStyleSheet("#container { background-color; #222 }")
        self.layout = QVBoxLayout()

        #Set Central Widget
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        #Show Window
        self.show()



    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        sys.exit(app.exec())



