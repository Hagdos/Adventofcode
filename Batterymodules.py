import sys
from PyQt5.QtCore    import Qt, QTimer
from PyQt5.QtGui     import QDoubleValidator, QPainter, QColor, QBrush, QFont
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QVBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit

class GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Battery configuration calculator')
        self.layout = QGridLayout()
        self.line = 0
        self.setGeometry(600,300, 820, 800)
        
        # Input for total number of cells
        self.addrowoflabels(["Minimum number of cells:", "Maximum number of cells:"])
        self.mincells = QLineEdit()
        self.maxcells = QLineEdit()
        self.addrowofinputs([self.mincells, self.maxcells], [str(32*104), str(32*104+20)])
           
        # Input for min and max voltages
        self.addrowoflabels(["Min. cell voltage [V]:", "Min. pack voltage [V]:"])
        self.minCellVolt = QLineEdit()
        self.minPackVolt = QLineEdit()
        self.addrowofinputs([self.minCellVolt, self.minPackVolt], ['2.8', '250'])
        
        self.addrowoflabels(["Max. cell voltage [V]:", "Max. pack voltage [V]:"])
        self.maxCellVolt = QLineEdit()
        self.maxPackVolt = QLineEdit()
        self.addrowofinputs([self.maxCellVolt, self.maxPackVolt], ['4.2', '450'])
        
        self.table = QTableWidget(3, 7)
        self.fillTable()
        
        
        self.layout.addWidget(self.table, self.line, 0, self.line, 2)
        self.layout.setRowStretch(self.line, 1000)
        
        self.setLayout(self.layout)
        self.show()
    
    def addrowoflabels(self, texts):
        self.column = 0
        for text in texts:
            self.layout.addWidget(QLabel(text), self.line, self.column)
            self.column += 1
        self.layout.setRowStretch(self.line, 1)
        self.line += 1
    
    def addrowofinputs(self, labels, texts):
        self.column = 0
        for i, label in enumerate(labels):
            label.setValidator(QDoubleValidator())
            label.textEdited.connect(self.inputchanged)
            try:
                label.setText(texts[i])
            except:
                label.setText('0')
            self.layout.addWidget(label, self.line, self.column)
            self.column += 1
        self.layout.setRowStretch(self.line, 1)
        self.line+=1

    def calcOptions(self):
        minseries = int(int(self.minPackVolt.text())//float(self.minCellVolt.text()))
        maxseries = int(int(self.maxPackVolt.text())//float(self.maxCellVolt.text()))
        
        data = dict()
        lines = 0
        # print(minseries,maxseries)
        
        for n in range(int(self.mincells.text()), int(self.maxcells.text())+1):
            options = []
            for series in range(minseries, maxseries+1):
                if n%series == 0:
                    parallel = n//series
                    divisors = [d for d in range(2, series) if series%d == 0]
                    Vmin = int(series * float(self.minCellVolt.text()))
                    Vmax = int(series * float(self.maxCellVolt.text()))
                    Vtyp = int(series * 3.6)
                    options.append((series, parallel, divisors, Vmin, Vmax, Vtyp))
            data[n] = options.copy()
            lines += len(options)
        
        return data, lines
    
    def fillTable(self):
        self.table.clear()
        data, length = self.calcOptions()
        self.table.setRowCount(length)
        self.table.setHorizontalHeaderLabels(['# of cells', 'Series', 'Parallel', 'Module series size options', 'Vmin', 'Vmax', 'Vtyp'])
        for c in range(7):
            self.table.setColumnWidth(c, 80)
        self.table.setColumnWidth(3, 300)
        line = 0
               
        for ncells in data.keys():                       
            for options in data[ncells]:
                self.table.setItem(line ,0, QTableWidgetItem(str(ncells)))
                for c, d in enumerate(options):
                    self.table.setItem(line ,c+1, QTableWidgetItem(str(d)))
                line+=1
            
        self.table.resizeRowsToContents()

    def inputchanged(self):
        self.fillTable()
        
        
    def keyPressEvent(self, keyEvent):
        super(GUI, self).keyPressEvent(keyEvent)
        key = keyEvent.key()
        if key == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication([])
    gui = GUI()
    sys.exit(app.exec_())
    