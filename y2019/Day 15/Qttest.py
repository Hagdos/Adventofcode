# Try not to include more than what you actually need
from sys import exit as sysExit
# import sys
from PyQt5.QtCore    import Qt
#from PyQt5.QtGui     import
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QPlainTextEdit, QHBoxLayout


#Taken from https://forum.qt.io/topic/103613/how-to-call-keypressevent-in-pyqt5-by-returnpressed/3
# class CenterObject(QPlainTextEdit):
#     def __init__(self):
#         QPlainTextEdit.__init__(self)

class CenterObject(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 355, 280)
        self.setWindowTitle('Brushes')
        self.show()

    def keyPressEvent(self, keyEvent):
        super(CenterObject, self).keyPressEvent(keyEvent)

        if keyEvent.key()  == Qt.Key_Down :
            print(' Down')
        elif keyEvent.key() == Qt.Key_Up :   
            print(' Up')
        elif keyEvent.key() == Qt.Key_Left :
            print(' Left')
        elif keyEvent.key() == Qt.Key_Right :
            print(' Right')   


class CenterPane(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        objCntrPane = CenterObject()
        hbox = QHBoxLayout(self)
        hbox.addWidget(objCntrPane)
 
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        winLeft = 100
        winTop = 100
        winWidth = 400
        winHeight = 300

        self.setWindowTitle('Main Window')
        self.setGeometry(winLeft, winTop, winWidth, winHeight)
        self.setCentralWidget(CenterObject())


if __name__ == "__main__":
    app = QApplication([])  

    GUI = CenterObject()
    # GUI.show()

    sysExit(app.exec_())
    
    
#Play by hand version!
    
    # def keyPressEvent(self, keyEvent):
    #     super(Game, self).keyPressEvent(keyEvent)
    #     key = keyEvent.key()
    #     if key in [Qt.Key_Up, Qt.Key_Down, Qt.Key_Right, Qt.Key_Left]:
    #         self.newx = self.userx
    #         self.newy = self.usery
    #         if key == Qt.Key_Up:
    #             self.inputs.append(1)
    #             self.newy -= 1
    #         elif key == Qt.Key_Down:
    #             self.inputs.append(2)
    #             self.newy += 1
    #         elif key == Qt.Key_Left:
    #             self.inputs.append(3)
    #             self.newx -= 1
    #         elif key == Qt.Key_Right:
    #             self.inputs.append(4)
    #             self.newx += 1
    #         self.mem, self.outputs, self.counters, self.finished = ic.runintcode(self.mem, self.inputs, self.counters)
            
    #         if self.outputs[-1] == 0:
    #             self.walls.append((self.newx, self.newy))
    #             # print("Wall")
    #         elif self.outputs[-1] == 1:
    #             self.path.append((self.userx, self.usery))
    #             self.userx = self.newx
    #             self.usery = self.newy
    #             # print("Move")
    #         elif self.outputs[-1] == 2:
    #             self.userx = self.newx
    #             self.usery = self.newy
    #             print("Ogygen System found!")
    #             self.finished = True
    #         self.update()