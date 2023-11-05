import os

def put_computer_to_sleep():
    if os.name == 'posix':
        os.system('sudo pmset sleepnow')
    elif os.name == 'nt':
        # For Windows
        os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
