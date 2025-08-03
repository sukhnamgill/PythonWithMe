from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from mutagen.id3 import ID3
from PIL import Image
from io import BytesIO
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

import sys
import os
import vlc
class Player(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.setGeometry(45,45,1000,500)
        # add listview
        self.l=QListWidget()
        self.l.setFixedSize(400, 600)
        self.l.setFont(QFont("Arial", 13))
        self.font = QFont("Arial", 30)

        # seek bar 
        self.seekbar=QSlider(Qt.Horizontal)


        label=QLabel("MUSIC PLAYER")

        label.setFont(self.font)
          # <<-- Your MP3 file name
        self.add_song=QPushButton("Add ")
        

        
         # two sub layouts
        self.layout1=QVBoxLayout()
        self.layout2=QVBoxLayout()

        # layout2 da sublayout
        self.hlayout=QHBoxLayout()
        self.h2layout=QHBoxLayout()
        self.volume=QDial()
        self.play_pause_btn=QPushButton()
        self.back_btn=QPushButton()
        
        self.next_btn=QPushButton()
        self.repeat=QCheckBox()

        # add icons to buttons
        self.back_btn.setIcon(QIcon("back.png"))
        self.play_pause_btn.setIcon(QIcon("play.png"))
        self.next_btn.setIcon(QIcon("next.png"))
        self.repeat.setIcon(QIcon("repeat.png"))
        self.repeat.setIconSize(QSize(30, 30))
      

        self.h2layout.addWidget(self.volume)

        self.h2layout.addWidget(self.back_btn)
        self.h2layout.addWidget(self.play_pause_btn)
        self.h2layout.addWidget(self.next_btn)
        self.h2layout.addWidget(self.repeat)


        self.layout2.addLayout(self.hlayout)
        self.layout2.addWidget(self.seekbar)
        
        self.layout2.addLayout(self.h2layout)
        # adding widgets to layout 1
        
        self.layout1.addWidget(label)
        self.layout1.addWidget(self.l)
        self.layout1.addWidget(self.add_song)

        # adding widgets to layout 2
        self.cover_label = QLabel("No Cover Found")
        pixmap=QPixmap("logo.jpg")
        self.cover_label.setScaledContents(True)
        self.cover_label.setPixmap(pixmap)
        self.cover_label.setScaledContents(True)
        self.cover_label.setFixedSize(400,500)
        self.hlayout.addWidget(self.cover_label)
        self.volume.setValue(50)

        # add css
        self.l.setStyleSheet('''border: 2px solid white;
                                    border-radius:20px;
                             padding:10px;
                             background-color:white;''')
        self.cover_label.setStyleSheet('''
                                    border: 2px solid black;
                                    border-radius:20px;
                                    padding:10px;
                                    background-color:black;''')
    
        
        self.timer1=QTimer()
        
        
        self.timer1.start(1000)
        self.timer1.timeout.connect(self.repeat_song)
    

        # add song with function
        self.seekbar.setRange(0, 100)  # Set the range of the seek bar
        self.seekbar.setValue(0)
        self.add_song.clicked.connect(self.addsong)
        self.seekbar.valueChanged.connect(self.seekbarchanged1)
        self.volume.valueChanged.connect(self.set_volume)
        self.play_pause_btn.clicked.connect(self.play_pasue)
        self.back_btn.clicked.connect(self.back_btn_func)
        self.next_btn.clicked.connect(self.next_btn_func)
        
        


 
        #layouts
        #main
        self.main_layout=QHBoxLayout()
        # add sub layout in to main layout
        self.main_layout.addLayout(self.layout1)
        self.main_layout.addLayout(self.layout2)

        self.setLayout(self.main_layout)
        self.l.clicked.connect(self.getlist)
          # Update every second
        
        # self.l.addItem('a.mp3')
        self.flag=False
        self.load=False
        # qtimer set for updating the seekbar
        
        

       

        # add css to layouts
        #functions
    
    def repeat_song(self):
        # print("started")
        
        j=self.repeat.isChecked()
        if self.load:
            if self.song.is_playing():
                    # print("song is playing")
                    # songtime=self.song.get_time()
                    # dur=self.song.get_length()
                    # dur=dur-1000
                    # print("song is playing")
                    jn=self.seekbar.value()
                    print(jn)
                    if jn>=99:
                        if(j==True):
                            curnt=self.l.currentRow()
                            self.l.setCurrentRow(curnt)
                            self.getlist()
                            # print("song is repeated played")
                        else:
                            # print("repeat mode is off")
                            curnt=self.l.currentRow()
                            curnt=curnt+1
                            self.l.setCurrentRow(curnt)
                            # print("next song played")
                            self.getlist()

                    else:
                        
                        print("song is playing")
        else:
            print("first play song")    
            
            
       
        
    def ch_speed(self):
        pass
    def next_btn_func(self):
        if self.load:
            current_index = self.l.currentRow()
            if current_index < self.l.count() - 1:
                new_index = current_index + 1
                self.l.setCurrentRow(new_index)
                self.getlist()
                print("Moved to next song:", self.l.currentItem().text())
            else:
                print("Already at the last song.")
        else:
            print("No song is currently loaded. Please select a song first.")
    def back_btn_func(self):
        if self.load:
            current_index = self.l.currentRow()
            if current_index > 0:
                new_index = current_index - 1
                self.l.setCurrentRow(new_index)
                self.getlist()
                print("Moved to previous song:", self.l.currentItem().text())
            else:
                print("Already at the first song.")
        else:
            print("No song is currently loaded. Please select a song first.")
    def play_pasue(self):
        if self.load:
            if self.song.is_playing():
                self.song.pause()
                # self.play_pause_btn.setText("Play")
                self.play_pause_btn.setIcon(QIcon("play.png"))

                print("Song paused")
            else:
                self.song.play()
                # self.play_pause_btn.setText("Pause")
                self.play_pause_btn.setIcon(QIcon("pause.png"))
                print("Song resumed")
        else:
            print("No song is currently loaded. Please select a song first.")
    def set_volume(self):
        volume = self.volume.value()
        if self.load:
            self.song.audio_set_volume(volume)
            print("Volume set to:", volume)
        else:
            print("No song is currently playing. Cannot set volume.")
    def set_duration(self, duration):
        self.seekbar.setRange(0, duration)
    def update_slider(self):
        if self.load and self.song.is_playing():
            try:
            # Get duration in milliseconds
                duration = self.song.get_length()
                # print(duration)
                if duration <= 0:
                    return
                
            
            # Get current time in milliseconds
                current_time = self.song.get_time()

            # Calculate percentage
                progress = int((current_time / duration) * 100)
                self.seekbar.blockSignals(True)  # Prevent triggering seekbarchanged1
                self.seekbar.setValue(progress)
                self.seekbar.blockSignals(False)

            except Exception as e:
                print("Error updating seekbar:", e)

    # def update_slider(self):
        
          # Increment the slider value by 1 every second


    # function for adding song
    def addsong(self):
        print("hello")
        self.fileopen=QFileDialog()      
        # self.layout1.addWidget(self.fileopen)
        self.l.clear()
        self.text,_=self.fileopen.getOpenFileNames(self,"Select Music Files")
        print(str(self.text))
        if self.text:
            self.l.clear()
            for file_path in self.text:
                file_name = os.path.basename(file_path)
                self.l.addItem(file_name)

    
    # function for playing song
    
    def getlist(self):
        # timer
        self.timer=QTimer()
        self.timer.timeout.connect(self.update_slider)
        self.timer.start(1000)

        # next 
        self.s=self.l.currentItem()
        j=self.s.text()
        # print(type(j))
        self.show_cover(self.text[self.l.currentRow()])
        if(self.flag==True):
            # print("song stop")
            # self.play_pause_btn.setText("Play")
            self.play_pause_btn.setIcon(QIcon("play.png"))

            self.song.stop()
            self.flag=True
            
            
            self.song=vlc.MediaPlayer(self.text[self.l.currentRow()])
            # self.show_cover(self, self.text[self.l.currentRow()])
            self.song.play()
            
            # self.play_pause_btn.setText("Pause")
            self.play_pause_btn.setIcon(QIcon("pause.png"))

            

        else:
            self.song=vlc.MediaPlayer(self.text[self.l.currentRow()])
            print(self.l.currentRow())

            self.song.audio_set_volume(50)
            self.song.play()
            self.load=True
            # print("song played1111")
            # self.play_pause_btn.setText("Pause")
            self.play_pause_btn.setIcon(QIcon("pause.png"))

            self.flag=True

    def show_cover(self, file_path):
        try:
             audio = ID3(file_path)
             for tag in audio.values():
                if tag.FrameID == "APIC":
                    image_data = tag.data
                    image = Image.open(BytesIO(image_data))
                    buffer = BytesIO()
                    image.save(buffer, format="PNG")
                    qimg = QImage.fromData(buffer.getvalue())
                    pixmap = QPixmap.fromImage(qimg)
                    self.cover_label.setPixmap(pixmap)
                     # Cover image frame
                        
        except Exception as e:
                print("Failed to load cover:", e)    
    def seekbarchanged1(self,position):
        if self.load==True:
            position = self.seekbar.value()
            # print(position)
            self.song.set_position(position/100)
            
            # Convert to a fraction (0.0 to 1.0)
            
            
        else:

            print("No song is currently playing.")  
def main():
    app=QApplication(sys.argv)
    win=Player()
   
    win.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()
