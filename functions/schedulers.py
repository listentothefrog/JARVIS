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
    
schedule.every().day.at("05:46").do(wake_up)
schedule.every().day.at("05:48").do(start_focus_session)
schedule.every().day.at("06:30").do(end_focus_session)
schedule.every().day.at("16:00").do(send_updates_from_calendar)
schedule.every().day.at("17:00").do(break_function)
schedule.every().day.at("17:05").do(start_focus_session)
schedule.every().day.at("17:40").do(break_function)
schedule.every().day.at("17:50").do(start_focus_session)
schedule.every().day.at("19:00").do(start_gym_focus)
schedule.every().day.at("19:45").do(start_focus_session)
schedule.every().day.at("22:00").do(end_focus_session)
schedule.every().day.at("22:10").do(bed_time_wrapup) 

while True:
    schedule.run_pending()
    time.sleep(10)