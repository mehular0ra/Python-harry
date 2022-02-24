from pygame import mixer
import time

def play_music(song):
    # Starting the mixer
    mixer.init()

    # Loading the song
    mixer.music.load(song)
    
    # Setting the volume
    mixer.music.set_volume(0.8)
    
    # Start playing the song
    mixer.music.play()

def play_music1():
    play_music("Song1.mp3")
def play_music2():
    play_music("Song2.mp3")
def play_music3():
    play_music("Song3.mp3")


def stop_music():
    # Stop the mixer
    mixer.music.stop()

if __name__ == '__main__':
    play_music1()
    time.sleep(3)
    mixer.music.stop()
    

  

