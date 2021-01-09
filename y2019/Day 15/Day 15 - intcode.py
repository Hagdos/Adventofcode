from sys import path
from sys import exit as sysExit
if "D:\Mijn Documenten\AdventofCode\y2019" not in path:
    path.append("D:\Mijn Documenten\AdventofCode\y2019")
import intcode as ic
from PyQt5.QtCore    import Qt, QTimer
from PyQt5.QtGui     import QPainter, QColor, QBrush, QFont
from PyQt5.QtWidgets import QApplication, QWidget

class Game(QWidget):
    def __init__(self, mem):
        QWidget.__init__(self)
        #Dictionary of blocks. 0 is a wall, 1 is an open space, 2 is oxygenthing, 3 is a deadendpath, 4 is a path after finding
        self.blocks = {}
        self.timestep = 1         #Time between steps
        self.bs = 20                #Blocksize
        self.directions = [(1, 0, -1), (2, 0, 1), (3, -1, 0), (4, 1, 0)]
        self.directions.reverse()
        self.userx = 25
        self.usery = 25
        self.initx = self.userx
        self.inity = self.usery
        self.blocks[self.userx, self.usery] = 1
        self.show()
        self.mem = mem
        self.counters = [0, 0, 0, 0]
        self.finished = False
        self.found = False
        self.paused = False
        self.inputs = []
        self.setGeometry(0, 30, self.bs*50, self.bs*50)
        self.clockinit()
        self.steps = 0
        self.minutes = 0
   
    def clockinit(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.playgame)
        self.timer.start(self.timestep)        
            
    def playgame(self):
        if not self.finished:
            self.determineInput()
            #Run the game
            if not self.finished:
                self.mem, self.outputs, self.counters, self.finished = ic.runintcode(self.mem, self.inputs, self.counters)  
            self.handleOutput()
            
    def fillOxygenInit(self):
        self.userx = self.oxygenLocation[0]
        self.usery = self.oxygenLocation[1]
        self.timestep = 10
        self.timer.timeout.disconnect(self.playgame)
        self.timer.timeout.connect(self.fillOxygen)
        self.timer.start(self.timestep)
        
    def fillOxygen(self):
        self.finished = True
        for block in self.blocks:
            if self.blocks[block] == 2:
                for (direction, dx, dy) in self.directions:
                    if self.blocks[(block[0]+dx, block[1]+dy)] == 3:
                        self.finished = False
                        self.blocks[(block[0]+dx, block[1]+dy)] = 5
        for block in self.blocks:
            if self.blocks[block] == 5: 
                self.blocks[block] = 2
        if self.finished:
            self.timer.stop()
        else:
            self.minutes += 1
            self.update()

                            
    def determineInput(self):
        keys = self.blocks.keys()
        self.newx = self.userx
        self.newy = self.usery        
        self.newinput = 0
        for (direction, dx, dy) in self.directions:
            if (self.userx+dx, self.usery+dy) not in keys:
                self.newinput  = direction
                self.newx += dx                
                self.newy += dy
                break
        if self.newinput == 0:
            for (direction, dx, dy) in self.directions:
                if self.blocks[(self.userx+dx, self.usery+dy)] == 1:
                    if self.found:
                        if not self.blocks[(self.userx, self.usery)] == 2:
                            self.blocks[(self.userx, self.usery)] = 3
                            # self.blocks[(self.userx, self.usery)] = 3                        
                    else:
                        self.blocks[(self.userx, self.usery)] = 3
                    self.newinput  = direction
                    self.newx += dx                
                    self.newy += dy
                    break
           
        if self.newinput  == 0:
            print("Mapped!")
            self.finished = True
            self.found = False
            self.newinput = 1
            self.timer.stop()
            self.fillOxygenInit()
            self.update()
        self.inputs.append(self.newinput)
  
        
    def handleOutput(self):
        self.blocks[(self.newx, self.newy)] = self.outputs[-1]
        if self.outputs[-1] == 1:
            self.userx = self.newx
            self.usery = self.newy
        elif self.outputs[-1] == 2:
            self.userx = self.newx
            self.usery = self.newy
            print("Oxygen System found!")
            self.oxygenLocation = (self.userx, self.usery)
            # self.finished = True
            self.found = True
        self.update()    
               
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawWalls(qp)
        self.drawUser(qp)
        self.drawMinutes(qp)
        # if self.finished:
        #     self.drawWinText(qp)
        qp.end()
        
    def keyPressEvent(self, keyEvent):
        super(Game, self).keyPressEvent(keyEvent)
        key = keyEvent.key()
        
        if key == Qt.Key_Space:
            if self.paused:
                self.timer.start(self.timestep)
                self.paused = False
            else:
                self.timer.stop()
                self.paused = True
        elif key == Qt.Key_Escape:
            self.close()
        elif key == Qt.Key_Plus:
            self.timestep /= 2
            self.timer.start(self.timestep)
        elif key == Qt.Key_Minus:
            self.timestep *= 2
            self.timer.start(self.timestep)
    
        if key in [Qt.Key_Up, Qt.Key_Down, Qt.Key_Right, Qt.Key_Left]:
            self.steps += 1
            self.newx = self.userx
            self.newy = self.usery
            if key == Qt.Key_Up:
                self.inputs.append(1)
                self.newy -= 1
            elif key == Qt.Key_Down:
                self.inputs.append(2)
                self.newy += 1
            elif key == Qt.Key_Left:
                self.inputs.append(3)
                self.newx -= 1
            elif key == Qt.Key_Right:
                self.inputs.append(4)
                self.newx += 1
            self.mem, self.outputs, self.counters, self.finished = ic.runintcode(self.mem, self.inputs, self.counters)
            self.handleOutput()   
            print(self.steps)
       
    def drawWalls(self, qp):
        for block in self.blocks:
            if self.blocks[block] == 0:
                qp.setBrush(QBrush(Qt.SolidPattern))
            if self.blocks[block] == 1:
                qp.setBrush(QBrush(Qt.Dense7Pattern))
            if self.blocks[block] == 2:
                brush = QBrush(Qt.Dense1Pattern)
                brush.setColor(QColor("Green"))
                qp.setBrush(brush)
            if self.blocks[block] == 3:
                brush = QBrush(Qt.Dense4Pattern)
                brush.setColor(QColor("Red"))
                qp.setBrush(brush)
            if self.blocks[block] == 4:
                brush = QBrush(Qt.Dense4Pattern)
                brush.setColor(QColor("Green"))
                qp.setBrush(brush)
            qp.drawRect(block[0]*self.bs, block[1]*self.bs, self.bs, self.bs)    

    def drawUser(self, qp):
        qp.setBrush(QBrush(Qt.DiagCrossPattern))
        qp.drawRect(self.userx*self.bs, self.usery*self.bs, self.bs, self.bs)
        
        
    def drawMinutes(self, qp):
        qp.setFont(QFont('Decorative', self.bs))
        qp.drawText(0, 47*self.bs, "Minutes passed: {}".format(self.minutes)) 
        
    def drawWinText(self, qp):
        qp.setPen(QColor("Red"))
        qp.setFont(QFont('Decorative', 30))
        if self.found:
            qp.drawText(250, 500, "Oxygen system found! Location ({}, {})".format(self.userx-self.initx, self.usery-self.inity))  
            ans = 0    #minus one to account for the starting position
            for loc in self.blocks:
                if self.blocks[loc] == 1:
                    ans+=1
            print("Answer to part 1:", ans)
        else:
            qp.drawText(250, 500, "Mapping finished")  
            
            
f = open('code.txt')
code = f.readline().strip().split(',')
mem = ic.codetomem(code)

app = QApplication([])  
GUI = Game(mem)
sysExit(app.exec_())
