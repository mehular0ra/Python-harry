import numpy as np
import datetime


def get_water_time(): 
    lst = [(10+i, 1) for i in range(10)]
    return lst

def get_eye_time():
    lst = [(9+i/2, 30 if i%2==1 else 0) for i in range(1, 10)]
    # lst.remove((18, 0))
    return lst

def get_exercise_time():
    lst = [(9, 45), (10, 30), (11, 15), (12, 0), (12, 45), (13, 30), (14, 15), (15, 0), (15, 45), (16, 30),
    (17, 45)]

def break_type(type):
    current_time = datetime.datetime.now() 
    time_arr = list(type())
    curr_time_lst = (current_time.hour, current_time.minute, current_time.second)
    return True if curr_time_lst in time_arr else False

def water_break():
    return break_type(get_water_time)
    
def eye_break():
    return break_type(get_eye_time)

def exercise_break():
    return break_type(get_exercise_time)


# confirming actions
def confirm_water():
    resp = input("Did you drink water (enter drank if yes): ")
    return True if resp=='drank' else False

def confirm_eye():
    resp = input("Did you do eye ex (enter EyDone if done): ")
    return True if resp=='EyDone' else False

def confirm_exercise():
    resp = input("Did you do exercise (enter EXDone if done): ")
    return True if resp=='ExDone' else False


def work_end():
    current_time = datetime.datetime.now() 
    curr_time_lst = (current_time.hour, current_time.minute, current_time.second)
    if curr_time_lst == (18, 0, 0):
        return True


if __name__ == '__main__':
    # Printing attributes of now(). 
    current_time = datetime.datetime.now() 
    print(current_time.hour)
    print(current_time.minute)


    arr = 10 + np.array([1, 3, 4])
    print(arr)
