from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import vlc

import sys
class dj(QWidget):
    def __init__(self, parent = None):
        super(dj,self).__init__(parent)
        self.setGeometry(50,60,600,600)
        supermain=QVBoxLayout()
        mainlayout=QHBoxLayout()
        self.left_play=QPushButton("Left Play")
        mainlayout.addWidget(self.left_play)
        self.left_play.clicked.connect(self.play_left)
        self.volume=QDial()
        mainlayout.addWidget(self.volume)
        self.volume.valueChanged.connect(self.volume_changed)
        # mainlayout.addWidget(QSpinBox())
        self.rt_play=QPushButton("Right play")
        mainlayout.addWidget(self.rt_play)
        self.rt_play.clicked.connect(self.rt_play1)
        self.rightsongvolume=QDial()
        mainlayout.addWidget(self.rightsongvolume)
        self.rightsongvolume.valueChanged.connect(self.volume_changednew)
        # mainlayout.addWidget(QSpinBox())
        self.list=QListWidget()
        self.list.addItem("hello")

        self.file=QFileDialog()
        # supermain.addWidget(self.file)
        supermain.addWidget(self.list)
        supermain.addLayout(mainlayout)
        self.song=vlc.MediaPlayer("a.mp3")
        self.song2=vlc.MediaPlayer("b.mp3")
        layoutq=QHBoxLayout()
        # supermain.addLayout(layoutq)
        self.label=QLabel("0")
        
        self.master=QDial(self)
        self.master.setValue(50)
        
        layoutq.addWidget(self.master)
        layoutq.addWidget(self.label)
        self.main_play_pause=QPushButton("Play/Pause")
        layoutq.addWidget(self.main_play_pause)
        self.main_play_pause.clicked.connect(self.main_play)
        mainlayout.addLayout(layoutq)
        self.master.valueChanged.connect(self.getvalue)
        self.setLayout(supermain)
        self.isplay=False
        self.mainplay=False
        self.right_paly=False
    def volume_changednew(self):
        value = self.rightsongvolume.value()
        print("Right song volume changed to:", value)
        self.song2.audio_set_volume(value)
    def volume_changed(self):
        value = self.volume.value()
        print("Volume changed to:", value)
        self.song.audio_set_volume(value)
    def rt_play1(self):
        if self.right_paly==False:
            print("right song playing")
            self.song.play()
            self.right_paly=True
        else:
            print("right song paused")
            self.right_paly=False
            self.song.pause()

    def main_play(self):
        if self.mainplay==True:
            print("right left paused")
            self.mainplay=False
        else:
            print("right left  palyed")
            self.mainplay=True
    def play_left(self):
        if self.isplay==True:
            print("Left song paused")
            self.song2.pause()
            self.isplay=False
        else:
            print("left song played")
            self.isplay=True
            self.song2.play()

        
        
    def filefetch(self):
        j=self.file.getOpenFileNames()
            
        print( "file name is ",j)
        j=str(j)
        j=j.split(',')
        print(j)
        li=[]
        for i in j:
            print(i)
            li.append(i)
        self.list.addItems(li)


        print("hello")
            
            
    def getvalue(self):
        a=self.master.value()
        print("the value is ",a)
        
        b=a
        a=a-100
        a=a*a/100
        a=round(a)
        b=round(b)
        self.song.audio_set_volume(a)
        self.song2.audio_set_volume(b)
        self.label.setText(f"{a} {b}")


             
    


        

        
        
        
    
        
        

def run():
    app=QApplication(sys.argv)
    hello=dj()
    hello.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    run()