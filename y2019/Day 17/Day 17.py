from sys import path
from sys import exit as sysExit
if "D:\Mijn Documenten\AdventofCode\y2019" not in path:
    path.append("D:\Mijn Documenten\AdventofCode\y2019")
import intcode as ic
from PyQt5.QtCore    import Qt, QTimer
from PyQt5.QtGui     import QPainter, QColor, QBrush, QFont
from PyQt5.QtWidgets import QApplication, QWidget

#Print display:
def printdisplay(outputs):    
    disp = [[[]]]
    n = 0
    line = 0
    for i, o in enumerate(outputs):
        if o == 10:
            # print(''.join(disp[n][line]))
            disp[n].append([])
            line+=1
            if outputs[i-1] == 10:
                disp.append([[]])
                n+=1
                line = 0
        else:
            disp[n][line].append(chr(o))
    # print(''.join(disp[n][line]))
    return disp

#Open and run code
f = open('code.txt')
code = f.readline().strip().split(',')
mem = ic.codetomem(code)
mem, outputs, counters, finished = ic.runintcode(mem)
    
disp = printdisplay(outputs)
 
#Loop over all parts of the displaymatrix. If the dot is a #, it's not on the edge and there's a # on all four sides; it's a crossroad
xmax = len(disp[0][0])-1
ymax = len(disp[0])-1
ans = 0
for y, line in enumerate(disp[0]):
    for x, s in enumerate(line):
        cross = False
        if s == '^':
            loc = [x,y]
        if s == '#':
            if 0<x<xmax and 0<y<ymax:
                cross = True
                for (dx,dy) in [(-1,0), (1, 0), (0, -1), (0, 1)]:
                    # print(x,y,dx,dy)
                    if disp[0][y+dy][x+dx] != '#':
                        cross = False
                        break
                
                if cross:
                    ap = x*y #Calculate alignment parameter
                    ans += ap
  
# print("Answer to Part 1:", ans)

# =============================================================================
# Part 2
# =============================================================================

class Display(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.bs = 20                #Blocksize
        x = len(disp[0][0])
        y = len(disp[0])
        self.n = 0                  #Display number
        self.setGeometry(1700, 100, self.bs*x, self.bs*y)
        self.directions = [(1, 0, -1), (2, 0, 1), (3, -1, 0), (4, 1, 0)]
        self.timestep = 100
        self.clockinit()
        self.show()



    def clockinit(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(self.timestep) 
        self.paused = False

    def paintEvent(self, event):
        # print("Paint!")
        qp = QPainter()
        qp.begin(self)
        if self.n == 1:
            self.n += 1
        if self.n>=len(disp):
            self.n = 0
        line = 0
        column = 0
        for line, bl in enumerate(disp[self.n]):
            column = 0
            for block in bl:
                if block == '.':
                    qp.setBrush(QBrush(Qt.Dense7Pattern))
                    qp.drawRect(column*self.bs, line*self.bs, self.bs, self.bs)  
                    column += 1
                elif block == '#':
                    qp.setBrush(QBrush(Qt.SolidPattern))
                    qp.drawRect(column*self.bs, line*self.bs, self.bs, self.bs)  
                    column += 1
                elif block in ['^', '>', '<', 'v']:
                    brush = QBrush(Qt.SolidPattern)
                    brush.setColor(QColor("Green"))
                    qp.setBrush(brush)
                    qp.drawRect(column*self.bs, line*self.bs, self.bs, self.bs) 
                    qp.setBrush(QBrush(Qt.SolidPattern))
                    if block == '^':
                        qp.drawRect(column*self.bs+self.bs//10*4, line*self.bs, self.bs//5, self.bs//5)
                    elif block == '<':
                        qp.drawRect(column*self.bs, line*self.bs+self.bs//10*4, self.bs//5, self.bs//5)
                    elif block == '>':
                        qp.drawRect(column*self.bs+self.bs//5*4, line*self.bs+self.bs//10*4-self.bs//10, self.bs//5, self.bs//5)
                    elif block == 'v':
                        qp.drawRect(column*self.bs+self.bs//10*4, line*self.bs+self.bs//5*4, self.bs//5, self.bs//5)
                    column += 1
                elif block == 'X':
                    brush = QBrush(Qt.SolidPattern)
                    brush.setColor(QColor("Red"))
                    qp.setBrush(brush)
                    qp.drawRect(column*self.bs, line*self.bs, self.bs, self.bs)  
                    column += 1
                else:
                    print(block)
        qp.end()
        self.n+=1
        
    def keyPressEvent(self, keyEvent):
        super(Display, self).keyPressEvent(keyEvent)
        key = keyEvent.key()
        if key == Qt.Key_Escape:
            self.close()
        if key == Qt.Key_Space:
            if self.paused:
                self.timer.start(self.timestep)
                self.paused = False
            else:
                self.timer.stop()
                self.paused = True

foundend = False
path = []
d = 0
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
chart = disp[0][:-2]
xmax = len(chart[0])-1
ymax = len(chart)-1

# =============================================================================
# Find the path
# =============================================================================
while not foundend:
    try:
        if 0<=loc[1]+directions[d][1]<=ymax and 0<=loc[0]+directions[d][0]<=xmax and chart[loc[1]+directions[d][1]][loc[0]+directions[d][0]] == '#':
            path.append('F')
            loc[0] += directions[d][0]
            loc[1] += directions[d][1]
        elif 0<=loc[1]+directions[(d+1)%4][1]<=ymax and 0<=loc[0]+directions[(d+1)%4][0]<=xmax and chart[loc[1]+directions[(d+1)%4][1]][loc[0]+directions[(d+1)%4][0]] == '#':
            path.append('R')
            d = (d+1)%4
        elif 0<=loc[1]+directions[(d-1)%4][1]<=ymax and 0<=loc[0]+directions[(d-1)%4][0]<=xmax and chart[loc[1]+directions[(d-1)%4][1]][loc[0]+directions[(d-1)%4][0]] == '#':
            path.append('L')
            d = (d-1)%4
        else:
            foundend = True
        # break
    except:
        print(loc, d)
        foundend = True

# =============================================================================
# Condens the path
# =============================================================================

i = 0
stop = False
cpath = []
while not stop and i<1000:
    if i>=len(path):
        stop=True
    elif path[i] in ['R', 'L']:
        cpath.append(path[i])
        # cpath.append(',')
        i += 1
    elif path[i] == 'F':
        a = 1
        i += 1
        while i< len(path) and path[i] == 'F' and a<100:
            i+=1
            a+=1
        cpath.append(str(a))
        # cpath.append(',')

# print(','.join(cpath))

# =============================================================================
# Trial input
# =============================================================================
# trialpath = 'R,8,R,8,R,4,R,4,R,8,L,6,L,2,R,4,R,4,R,8,R,8,R,8,L,6,L,2'
# cpath =[]
# for s in trialpath:
#     if s != ',':
#         cpath.append(s)
# Trial input 2
# trialpath = 'R4,L10,L10,L8,R12,R10,R4,R4,L10,L10,L8,R12,R10,R4,R4,L10,L10,L8,L8,R10,R4,L8,R12,R10,R4,L8,L8,R10,R4,R4,L10,L10,L8,L8,R10,R4'
# cpath = []
# for s in trialpath.split(','):
#     cpath.append(s[0])
#     cpath.append(s[1:])
        

steps= set()
for i in range(0, len(cpath), 2):
    print(cpath[i], cpath[i+1])
    steps.add((cpath[i], cpath[i+1]))
    
print(steps)

# # cpath = path #Decompress the path, for a trial...
# length = 9
# step = 2
# solutions = []
# for la in range(2,length,step):
#     # trypath = cpath[:]
#     FA = cpath[:la]
#     for lb in range(2,length,step):
#         FB = cpath[la:la+lb]
#         for lc in range(2,length,step):
#             FC = cpath[la+lb:la+lb+lc]
#             trypath = cpath[:]
#             while trypath != []:
#                 if trypath[:la] == FA:
#                     trypath = trypath[la:]
#                 elif trypath[:lb] == FB:
#                     trypath = trypath[lb:]
#                 elif trypath[:lc] == FC:
#                     trypath = trypath[lc:]
#                 else:
#                     # print("Q", trypath)
#                     break
#             if not trypath:
#                 # print("Yes!")
#                 solutions.append([FA, FB, FC])
            
#             print("Trial:")
#             print("FA: ", FA)
#             print("FB: ", FB)
#             print("FC: ", FC)
#             print(','.join(cpath))
#             print(','.join(trypath))
#             # print(bool(trypath))
#             print()
            
            

            
# print("Solutions")
# [print(s) for s in solutions]
                
# for s in solutions:
#     print('FA: ', s[0])
#     print('FB: ', s[1])
#     print('FC: ', s[2])
#     print()
# print(solutions)
                
mem = ic.codetomem(code)
mem[0] = 2

# #Functions:
FA = 'R,12,L,10,L,10'
FB = 'L,6,L,12,R,12,L,4'
FC = 'L,12,R,12,L,6'

#Functioncalls:
Call = 'A,B,A,B,C,B,C,A,C,C'

Feed = 'y'

inputs = []
for c in Call:
    inputs.append(ord(c))
inputs.append(ord('\n'))
# inputs.append(ord(','))
for F in [FA, FB, FC]:
    for i in F:
        inputs.append(ord(i))
    inputs.append(ord('\n'))
    # inputs.append(ord(','))
inputs.append(ord(Feed))
# inputs.append(ord(','))
inputs.append(ord('\n'))

counters = [0,0,0,0]
finished = False

mem, outputs, counters, finished = ic.runintcode(mem, inputs, counters)

disp = printdisplay(outputs[:-1])


app = QApplication([])  
display = Display()
sysExit(app.exec_())