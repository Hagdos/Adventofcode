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
        self.walls = []
        self.path = []
        self.foundblocks = []
        self.timestep = 0         #Time between steps
        self.bs = 20                #Blocksize
        self.userx = 25
        self.usery = 25
        self.initx = self.userx
        self.inity = self.usery
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
   
    def clockinit(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.playgame)
        self.timer.start(self.timestep)        
            
    def playgame(self):
        i = 0
        if not self.finished and i<10:
            i+=1
            self.determineInput()
            #Run the game
            if not self.finished:
                self.mem, self.outputs, self.counters, self.finished = ic.runintcode(self.mem, self.inputs, self.counters)  
            self.handleOutput()
                            
    def determineInput(self):
        self.newx = self.userx
        self.newy = self.usery        
        self.newinput = 0
        #TODO: Walk back over path if no unblocked path found
        for i, (dx, dy) in enumerate([(0, -1), (0, 1), (-1, 0), (1, 0)]): 
            if (self.userx+dx, self.usery+dy) not in self.walls+self.path:
                self.newinput  = i+1
                self.newx += dx                
                self.newy += dy
                break
        if self.newinput == 0:
            for i, (dx, dy) in enumerate([(0, -1), (0, 1), (-1, 0), (1, 0)]): 
                if (self.userx+dx, self.usery+dy) not in self.walls:
                    if self.found:
                        self.foundblocks.append((self.userx, self.usery))
                    self.walls.append((self.userx, self.usery))
                    self.newinput  = i+1
                    self.newx += dx                
                    self.newy += dy
                    break
           
        if self.newinput  == 0:
            print("Stuck!")
            self.finished = True
            self.found = False
            self.newinput = 1
        self.inputs.append(self.newinput)
  
        
    def handleOutput(self):
        if self.outputs[-1] == 0:
            self.walls.append((self.newx, self.newy))
            # print("Wall")
        elif self.outputs[-1] == 1:
            self.path.append((self.userx, self.usery))
            self.userx = self.newx
            self.usery = self.newy
            # print("Move")
        elif self.outputs[-1] == 2:
            self.path.append((self.userx, self.usery))
            self.userx = self.newx
            self.usery = self.newy
            print("Ogygen System found!")
            self.oxygenLocation = (self.userx, self.usery)
            self.finished = True
            self.found = True
        self.update()    
               
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawWalls(qp)
        self.drawPath(qp)
        self.drawFoundPath(qp)
        self.drawOxygen(qp)
        self.drawUser(qp)
        if self.finished:
            self.drawWinText(qp)
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
        qp.setBrush(QBrush(Qt.SolidPattern))
        for wall in self.walls:
            if wall not in self.path:
                qp.drawRect(wall[0]*self.bs, wall[1]*self.bs, self.bs, self.bs)
            
    def drawPath(self, qp):
        qp.setBrush(QBrush(Qt.Dense7Pattern))
        for pos in self.path:
            if pos not in self.walls:
                qp.drawRect(pos[0]*self.bs, pos[1]*self.bs, self.bs, self.bs)
            
    def drawFoundPath(self, qp):
        brush = QBrush(Qt.Dense4Pattern)
        brush.setColor(QColor("Red"))
        qp.setBrush(brush)
        for pos in self.path:
            if pos in self.walls:
                qp.drawRect(pos[0]*self.bs, pos[1]*self.bs, self.bs, self.bs)
        brush.setColor(QColor("Green"))
        qp.setBrush(brush)
        for pos in self.foundblocks:
            qp.drawRect(pos[0]*self.bs, pos[1]*self.bs, self.bs, self.bs)
    
    def drawUser(self, qp):
        qp.setBrush(QBrush(Qt.DiagCrossPattern))
        qp.drawRect(self.userx*self.bs, self.usery*self.bs, self.bs, self.bs)
        
    def drawOxygen(self, qp):
        if self.found:
            brush = QBrush(Qt.Dense1Pattern)
            brush.setColor(QColor("Green"))
            qp.setBrush(brush)
            qp.drawRect(self.oxygenLocation[0]*self.bs, self.oxygenLocation[1]*self.bs, self.bs, self.bs)
        
    def drawWinText(self, qp):
        qp.setPen(QColor("Red"))
        qp.setFont(QFont('Decorative', 50))
        if self.found:
            qp.drawText(500, 500, "Oxygen system found! Location {} {}".format(self.userx-self.initx, self.usery-self.inity))  
            ans = -1    #minus one to account for the starting position
            for loc in self.path:
                if loc not in self.walls:
                    ans+=1
            print("Answer to part 1:", ans)
        else:
            qp.drawText(500, 500, "Got stuck")  
            
            
f = open('code.txt')
code = f.readline().strip().split(',')
mem = ic.codetomem(code)

app = QApplication([])  
GUI = Game(mem)
sysExit(app.exec_())

#232 is too high, 231 ook
#226