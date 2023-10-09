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
from focus import start_focus


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
BOT_TOKEN = os.getenv('TOKEN')
from datetime import datetime

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.display_name}')

@bot.event
async def on_message(message):
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        if current_time == "05:48:00":
            start_focus(message.authour)

        time.sleep(1) 