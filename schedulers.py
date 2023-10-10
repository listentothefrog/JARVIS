# Todos
# 5:48 AM Start focus session 
# 6:30 AM End focus session, turn off computer, shower process 
# 4:00 PM Start computer, start focus session, homework process
# 5:00 PM Start sending notifcations on any remaining events in calendar
# 5:30 PM Start break functions till 5:40 PM 
# 5:40 PM Start focus session till 7:00 PM 
# 7:00 PM - 8:30 PM Start gym functions 
# 9:00 PM - 9:45 PM Start focus session function
# 9:46 PM Start bed time wrapup, turns off internet.

import discord
from discord.ext import commands, tasks
import os
import time
from dotenv import find_dotenv, load_dotenv
from functions.focus import start_focus
import schedule
from datetime import datetime

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
BOT_TOKEN = os.getenv('DUMMY_TOKEN')

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='$', intents=intents)

def print_function(): 
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"i runned, ran at -> {current_time}")
    

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.display_name}')
    
@bot.event
async def on_message(message): 
    if message.author == bot.user:
        return
    if message.content.startswith("$ping"): 
        await message.channel.send("hello world!")
        
    schedule.every().day.at("05:46").do(print_function)
    schedule.every().day.at("06:30").do(print_function)
    schedule.every().day.at("16:00").do(print_function)
    schedule.every().day.at("17:00").do(print_function)
    schedule.every().day.at("17:30").do(print_function)
    schedule.every().day.at("17:40").do(print_function)
    schedule.every().day.at("19:00").do(print_function)
    schedule.every().day.at("21:00").do(print_function)
    schedule.every().day.at("21:46").do(print_function)

bot.run(BOT_TOKEN)

while True: 
    schedule.run_pending()
    time.sleep(1)  
    
