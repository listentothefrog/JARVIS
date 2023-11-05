# Todos
# 4:00 PM Start focus session, fetch homework data from canvas and notion todos 
# 5:00 PM End focus session, turn off computer 
# 5:10 PM start focus session and open vs code
# 6:10 PM end focus session and close computer
# 7:30 PM start focus session 
# 8:30 PM end focus session 
# 8:30 PM - 9:30 PM start focus and open vs code and get any notion todos 
# 9:30 PM - Start bed time wrapup, turn off computer

import discord
from discord.ext import commands
import os
import asyncio
from dotenv import find_dotenv, load_dotenv
from datetime import datetime
from functions.focus import start_focus, end_focus
import time
from functions.get_news import get_top_news_articles
from functions.put_computer_to_sleep import put_computer_to_sleep

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
BOT_TOKEN = os.getenv('DUMMY_TOKEN')

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

async def send_dm_when_time_reached():
    await bot.wait_until_ready()

    while not bot.is_closed():
        current_time = datetime.now()
        
        if current_time.hour == 5 and current_time == 59: 
            # wake up computer goes here
            print("wake up function")
        
        
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.display_name}')
    bot.loop.create_task(send_dm_when_time_reached()) 

bot.run(BOT_TOKEN)
