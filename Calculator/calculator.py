import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

class Calculator(QWidget):
    op = ""
    def __init__(self):
        super().__init__()
        
        #create grid
        self.vbox = QVBoxLayout(self)
        
        self.hbox_input = QHBoxLayout()
        
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_fourth = QHBoxLayout()
        self.hbox_fifth = QHBoxLayout()
        
        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_fourth)
        self.vbox.addLayout(self.hbox_fifth)
        
        #create input line
        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)
        
        #create buttons
        #
        #     input line
        #    C   %  del  /      first row
        #    7   8   9   *      second row
        #    4   5   6   -      third row
        #    1   2   3   +      fourth row
        #    00  0   ,   =      fifth row
        #
        #1 row
        self.b_reset = QPushButton("C", self)
        self.hbox_first.addWidget(self.b_reset)
        self.b_percent = QPushButton("%", self)
        self.hbox_first.addWidget(self.b_percent)
        self.b_delete = QPushButton("del", self)
        self.hbox_first.addWidget(self.b_delete)
        self.b_divide = QPushButton("/", self)
        self.hbox_first.addWidget(self.b_divide)
        
        #2 row
        self.b_7 = QPushButton("7", self)
        self.hbox_second.addWidget(self.b_7)
        self.b_8 = QPushButton("8", self)
        self.hbox_second.addWidget(self.b_8)
        self.b_9 = QPushButton("9", self)
        self.hbox_second.addWidget(self.b_9)
        self.b_multiply = QPushButton("*", self)
        self.hbox_second.addWidget(self.b_multiply)
        
        #3 row
        self.b_4 = QPushButton("4", self)
        self.hbox_third.addWidget(self.b_4)
        self.b_5 = QPushButton("5", self)
        self.hbox_third.addWidget(self.b_5)
        self.b_6 = QPushButton("6", self)
        self.hbox_third.addWidget(self.b_6)
        self.b_minus = QPushButton("-", self)
        self.hbox_third.addWidget(self.b_minus)
        
        #4 row
        self.b_1 = QPushButton("1", self)
        self.hbox_fourth.addWidget(self.b_1)
        self.b_2 = QPushButton("2", self)
        self.hbox_fourth.addWidget(self.b_2)
        self.b_3 = QPushButton("3", self)
        self.hbox_fourth.addWidget(self.b_3)
        self.b_plus = QPushButton("+", self)
        self.hbox_fourth.addWidget(self.b_plus)
        
        #5 row
        self.b_00 = QPushButton("00", self)
        self.hbox_fifth.addWidget(self.b_00)
        self.b_0 = QPushButton("0", self)
        self.hbox_fifth.addWidget(self.b_0)
        self.b_dot = QPushButton(".", self)
        self.hbox_fifth.addWidget(self.b_dot)
        self.b_result = QPushButton("=", self)
        self.hbox_fifth.addWidget(self.b_result)
        
        
        #create button press action
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_00.clicked.connect(lambda: self._button("00"))
        
        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_multiply.clicked.connect(lambda: self._operation("*"))
        self.b_divide.clicked.connect(lambda: self._operation("/"))
        
        self.b_reset.clicked.connect(self._reset)
        self.b_delete.clicked.connect(self._delete)
        self.b_result.clicked.connect(self._result)
        self.b_percent.clicked.connect(lambda: self._button("%"))
        self.b_dot.clicked.connect(lambda: self._button("."))
    
    
    #create methods
    def _button(self, param):
        line = self.input.text()
        if param == "%":
            self.input.setText(str(float(line) / 100))
        elif param == ".":
            if line:
                self.input.setText(line + param)
            else:
                self.input.setText("0.")
        else:
            self.input.setText(line + param)
    
    def _operation(self, op):
        if(self.input.text()):
            self.num_1 = float(self.input.text())
            self.op = op
            self.input.setText("")
    
    def _reset(self):
        self.input.setText("")
    
    def _delete(self):
        line = self.input.text()
        if line:
            self.input.setText(line[0 : len(line) - 1])
    
    def _result(self):
        if self.input.text() and self.op:
            self.num_2 = float(self.input.text())
            if self.op == "+":
                self.input.setText(str(self.num_1 + self.num_2))
            elif self.op == "-":
                self.input.setText(str(self.num_1 - self.num_2))
            elif self.op == "/":
                if self.num_2 != 0:
                    self.input.setText(str(self.num_1 / self.num_2))
                else:
                    self.input.setText("Can't divide by 0")
            if self.op == "*":
                self.input.setText(str(self.num_1 * self.num_2))


#start app
app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())