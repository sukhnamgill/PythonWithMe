import vlc
from PyQt5.QtCore import QTimer
import time
# p=vlc.MediaPlayer("a.mp3")
# p.play()
# # p.pause()
# # print(p.pause())
# p.set_position(0.5)

# # p.set_speed(3)  
# # 
# timer=QTimer()


def trans(x):
    p=vlc.MediaPlayer(x)
    p.play()
    p.set_position(0.5)
    i=0
    for i in range(100):
        time.sleep(0.1)
        p.audio_set_volume(i)
    inp=input("enter something")
    p.stop()
trans("a.mp3")

    

# Set position to 50%

# time.sleep(100) 