from PyQt5 import QtWidgets, uic
import sys
import subprocess

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('layout.ui', self)
        self.show()

        ValueInfo = subprocess.Popen('brightnessctl'.split(), stdout=subprocess.PIPE)
        ValueInfoString = str(ValueInfo.communicate())

        CurrentValue = ValueInfoString[73:77]

        def ValueChange(self):
            level = LumSlider.value()
            CurrentValue100 = str(round(((level*100)/4882), 2))
            LevLabel.setText(str(level) + " / " + CurrentValue100 + "%")
            command = 'sudo brightnessctl s ' + str(level)
            subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            #output, error = process.communicate()
        
        LumSlider = self.findChild(QtWidgets.QSlider, 'LumSlider')
        LumSlider.setMinimum(100)
        LumSlider.setMaximum(4882)
        LumSlider.setValue(int(CurrentValue))
        LumSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        LumSlider.setTickInterval(200)
        LumSlider.valueChanged.connect(ValueChange)
        
        LevLabel = self.findChild(QtWidgets.QLabel, 'LevLabel')
        LevLabel.setText(str(LumSlider.value()) + " / " + str(round(((LumSlider.value()*100)/4882), 2)) + "%")

        def Set50(self):
            level = 2441
            CurrentValue100 = str(round(((level*100)/4882), 2))
            LevLabel.setText(str(level) + " / " + CurrentValue100 + "%")
            command = 'sudo brightnessctl s ' + str(level)
            subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            LumSlider.setValue(level)

        def Set100(self):
            level = 4882
            CurrentValue100 = str(round(((level*100)/4882), 2))
            LevLabel.setText(str(level) + " / " + CurrentValue100 + "%")
            command = 'sudo brightnessctl s ' + str(level)
            subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            LumSlider.setValue(level)

        self.Level50 = self.findChild(QtWidgets.QPushButton, 'Level50')
        self.Level50.clicked.connect(Set50)
        Level100 = self.findChild(QtWidgets.QPushButton, 'Level100')
        Level100.clicked.connect(Set100)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()