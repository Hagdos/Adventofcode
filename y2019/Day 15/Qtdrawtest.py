# Try not to include more than what you actually need
from sys import exit as sysExit

from PyQt5.QtCore    import Qt
from PyQt5.QtGui     import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout


class Game(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.walls = [(10,10), (11,12), (12,12)]
        self.bs = 20                #Blocksize
        self.userx = 20
        self.usery = 20
        self.show()
           
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawWalls(qp)
        self.drawUser(qp)
        self.drawText(qp)
        qp.end()
        
    def keyPressEvent(self, keyEvent):
        super(Game, self).keyPressEvent(keyEvent)
        key = keyEvent.key()
        if key in [Qt.Key_Up, Qt.Key_Down, Qt.Key_Right, Qt.Key_Left]:
            self.walls.append((15,15))
            self.update()
            print('Arrow')
        
    def drawWalls(self, qp):
        qp.setBrush(QBrush(Qt.SolidPattern))
        for wall in self.walls:
            qp.drawRect(wall[0]*self.bs, wall[1]*self.bs, self.bs, self.bs)
    
    def drawUser(self, qp):
        qp.setBrush(QBrush(Qt.DiagCrossPattern))
        qp.drawRect(self.userx*self.bs, self.usery*self.bs, self.bs, self.bs)
        
    def drawText(qp):
        


app = QApplication([])  

GUI = Game()

sysExit(app.exec_())

