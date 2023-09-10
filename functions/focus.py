import os
import webbrowser
import time
from humanfriendly import format_timespan
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

websites = ['www.youtube.com', "https://www.youtube.com", "www.instagram.com", "https://www.instagram.com/", "www.tiktok.com", "https://tiktok.com"]
start = time.time()
def start_focus():
    os.system("taskkill /im chrome.exe /f")
    with open(host_path, "r+") as fileptr: 
        content = fileptr.read()
        for website in websites: 
            if website in content: 
                pass
            else: 
                fileptr.write(redirect+"      "+website+"\n")
    print("blocked all entertainment websites")            
    webbrowser.open("https://www.notion.so/Assignments-Exams-0c3135345c6d4b6aabfc8a7150b55767")
def end_focus(): 
    end = time.time()
    os.system("taskkill /im chrome.exe /f")
    with open(host_path, 'r+') as fileptr:
            content=fileptr.readlines()
            fileptr.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    fileptr.write(line)
  
            # removing hostnmes from host file
            fileptr.truncate()
    
    print(f"the focus session lasted {format_timespan(end-start)}")
    print("unblocked all entertainment websites")
    webbrowser.open("https://www.notion.so/Assignments-Exams-0c3135345c6d4b6aabfc8a7150b55767")