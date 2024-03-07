from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list=[]

question_list.append(Question("Koliko je 3 + 3?", "6", "7", "33", "8"))
question_list.append(Question("Koliko ima kontinenata na svijetu?", "7", "6", "5", "2"))
question_list.append(Question("Koliko ja imam godina?", "12", "13", "14", "18"))
question_list.append(Question("U kojem gradu ja živim?", "Maglaju", "Brčkom", "Bjeljini", "Sarajevu"))
question_list.append(Question("Kada je dan prosvjetnih radnika?", "5", "7", "10", "8"))
question_list.append(Question("Kada je poceo prvi svjetski rat?", "1914", "1915", "1916", "1917"))
question_list.append(Question("Koji sam ja razred?", "7", "6", "5", "8"))
question_list.append(Question("Koliko je 3 - 2?", "1", "0", "33", "8"))
question_list.append(Question("Šta se nalazi u zoo vrtu?", "Životinje", "Ljudi", "Stvari", "Škola"))
question_list.append(Question("Kako se zove naš nastavnik?", "Milijan", "Dragan", "Ivan", "Faruk"))


app = QApplication([])
mywin = QWidget()
mywin.setWindowTitle('Memory card')
Button = QPushButton('Answer')
text = QLabel('Which nationality does not exist?')
RadioGroupBox = QGroupBox('Answer options')

rbtn_1 = QRadioButton('Enets')
rbtn_2 = QRadioButton('Chulyms')
rbtn_3 = QRadioButton('Smurfs')
rbtn_4 = QRadioButton('Aleuts')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("Test Result")
lb_Result = QLabel("Are you correct or not?")
lb_Correct = QLabel("The answer will be here!")

layout_res = QVBoxLayout()

layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment= Qt.AlignHCenter, stretch=2)

AnsGroupBox.setLayout(layout_res)

line = QVBoxLayout()
Hline1 = QHBoxLayout()
Hline2 = QHBoxLayout()
Hline3 = QHBoxLayout()

Hline1.addWidget(text, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
Hline2.addWidget(RadioGroupBox)
Hline2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
Hline1.addStretch(1)
Hline3.addWidget(Button, stretch = 1)
Hline3.addStretch(1)
line.addLayout(Hline1, stretch = 2)
line.addLayout(Hline2, stretch = 8)
line.addStretch(1)
line.addLayout(Hline3, stretch = 1)
line.addStretch(1)
line.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    Button.setText("Next question")

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    Button.setText("Answer")

    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()


def show_correct(res):
    lb_Result.setText(res)
    show_result()
    

def check_answer():
    if answers[0].isChecked():
        show_correct("Correct")
        mywin.score += 1
        print("Statistics\n- Total questions: ",mywin.total, "\n-Right answer: ",mywin.score)
        print("Rating: ", (mywin.score/mywin.total*100),"%")

    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Incorrect")
            print("Rating: ", (mywin.score/mywin.total*100),"%")

def next_question():
    mywin.total += 1
    print("Statistics\n- Total questions: ",mywin.total, "\n-Right answer: ",mywin.score)
    cur_question = randint(0, len(question_list)-1)
    q= question_list[cur_question]
    ask(q)

def click_OK():
    if Button.text() == "Answer":
        check_answer()
    else:
        next_question()


mywin.setLayout(line)

Button.clicked.connect(click_OK)
mywin.total = 0
mywin.score = 0
next_question()
mywin.show()
app.exec()