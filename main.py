############################
##IMPORTS
#############################
import sys
import os
from PySide2 import *
######################
##IMPORT GUI FILE
##########################
from ui_interface import *
##########################
#####################################
## MAIN WINDOW CLASS################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show
        ######################################################
        ## REMOVE WINDOWS TITLE BAR
        #######################################################
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ######################################################
        ## MAIN BACKGROUND TRANSPARANCY
        #######################################################
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ######################################################
        ## Shadow Effect Style
        #######################################################
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))
        ######################################################
        ## SET SHADOW TO CENTRAL WIDGET
        #######################################################
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        ######################################################
        ## SET WindowsIcon & Title
        #####################################################
        self.setWindowIcon(QtGui.QIcon(":/Icons/add.svg"))
        self.setWindowTitle("Dogma Indexer")
        #######################################################
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ####################################################
        ####MINIMIZE GRIP
        ###################################################
        QSizeGrip(self.ui.Size_Grip)
        ############################
        ## Minimize Window
        ####################################################
#########################################
## EXECUTE APP
##########################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
##########################################
