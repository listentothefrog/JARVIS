import os
import webbrowser
import time
from dotenv import find_dotenv, load_dotenv
from humanfriendly import format_timespan
from email.message import EmailMessage
import ssl
import smtplib

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
EMAIL_RECIVER = os.getenv('EMAIL_RECIVER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

email_sender = "emailsfromjarvis@gmail.com"
email_password = EMAIL_PASSWORD
email_reciver = EMAIL_RECIVER
    
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
    webbrowser.open("https://www.notion.so/Assignments-Exams-0c3135345c6d4b6aabfc8a7150b55767")
async def end_focus(user): 
    end = time.time()
    os.system("taskkill /im chrome.exe /f")
    with open(host_path, 'r+') as fileptr:
        content = fileptr.readlines()
        fileptr.seek(0)
        for line in content:
            if not any(website in line for website in websites):
                fileptr.write(line)
  
        # removing hostnames from the host file
        fileptr.truncate()
    
    await user.send(f"the focus session lasted {format_timespan(end-start)}")
    
    subject = "Focus Session Completed 🚀"
    body = f"I'm excited to share that Shashank has successfully completed a productive focus session. The session lasted {format_timespan(end-start)}. It's my part of keeping him focused, please respond with 'Yes' or 'No' to approve the end of his session."

    em = EmailMessage()
    em['From'] = email_sender
    em['To']= email_reciver
    em['Subject'] = subject
    em.set_content(body)
   
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciver, em.as_string())

    await user.send("i have just sent an email to Mr. Ellareddy for the approval for the end of your focus session. You'll be notified as soon as i get a response.")
    webbrowser.open("https://www.notion.so/Assignments-Exams-0c3135345c6d4b6aabfc8a7150b55767")