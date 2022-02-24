#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log
#
# Rules
# Pygame module to play audio

from play_music import play_music1, play_music2, play_music3, stop_music
from get_time import water_break, eye_break, exercise_break, confirm_water, confirm_eye, confirm_exercise, work_end

off = False
while (off == False):
    
    is_water_break = water_break()
    if (is_water_break):
        play_music1()
        if (confirm_water):
            stop_music()

    is_eye_break = eye_break()
    if (is_eye_break):
        play_music2()
        if confirm_eye():
            stop_music()

    is_exercise_break = exercise_break()
    if is_exercise_break():
        play_music3()
        if confirm_exercise():
            stop_music()

    if work_end():
        off = True

