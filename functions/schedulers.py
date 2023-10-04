# Todos
# 5:46 AM Wake up computer 
# 5:48 AM Start focus session 
# 6:30 AM End focus session, turn off computer, shower process 
# 4:00 PM Start computer, start focus session, homework process
# 5:00 PM Start sending notifcations on any remaining events in calendar
# 5:30 PM Start break functions till 5:40 PM 
# 5:40 PM Start focus session till 7:00 PM 
# 7:00 PM - 8:30 PM Start gym functions 
# 9:00 PM - 9:45 PM Start focus session function
# 9:46 PM Start bed time wrapup, turns off internet.

import schedule
import time


def wake_up(): 
    print("wake up function goes here") 
def start_focus_session(): 
    print("start focus")

def end_focus_session(): 
    print("end focus session")
    
def send_updates_from_calendar():
    print("send updates from calendars")

def break_function(): 
    print("start break") 
    
def start_gym_focus(): 
    print("start gym focus")

def bed_time_wrapup(): 
    print("start bed time wrapup functions") 
    

# schedule.every(2).seconds.do(task)
while True: 
    schedule.run_pending()
    time.sleep(1)
