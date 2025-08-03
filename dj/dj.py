import vlc
import time

# Create VLC player
player = vlc.MediaPlayer("a.mp3")

# Set volume (0 to 100)
player.audio_set_volume(70)

# Start playing
player.play()
print("Playing...")

time.sleep(5)

# Seek to 10 seconds
player.set_time(10000)  # in milliseconds

print("Jumped to 10s")

# Wait before ending
time.sleep(10)

player.stop()
