# Todos
# 6:00 AM Start focus session 
# 6:30 AM End focus session, turn off computer, shower process 
# 4:00 PM Start computer, start focus session, homework process
# 5:00 PM Start sending notifcations on any remaining events in calendar
# 5:30 PM Start break functions till 5:40 PM 
# 5:40 PM Start focus session till 7:00 PM 
# 7:00 PM - 8:30 PM Start gym functions 
# 9:00 PM - 9:45 PM Start focus session function
# 9:46 PM Start bed time wrapup, turns off internet.

import discord
from discord.ext import commands
import os
import asyncio
from dotenv import find_dotenv, load_dotenv
from datetime import datetime
from functions.focus import start_focus, end_focus
import time
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
            
        if current_time.hour == 6 and current_time.minute == 00:
            channel = bot.get_channel(1148273955728281683)
            if channel:
                await channel.send("Good Morning, Shashank. Starting a focus session ☀️")
                await start_focus(user="tren_brahh")  
            else:
                print("Channel not found.")
            await asyncio.sleep(60)  

        if current_time.hour == 6 and current_time.minute == 40: 
            channel = bot.get_channel(1148273955728281683)
            if channel:
                await channel.send("Ending focus session")
                await end_focus(user="tren_brahh")
                put_computer_to_sleep()  
            else:
                print("Channel not found.")
            await asyncio.sleep(60)
        
        if current_time.hour == 16 and current_time.minute == 00: 
            channel = bot.get_channel(1148273955728281683)
            if channel:
                await channel.send("Ending focus session")
                await end_focus(user="tren_brahh")  
            else:
                print("Channel not found.")
            await asyncio.sleep(60)
            
        if current_time.hour == 17 and current_time.minute == 00: 
            channel = bot.get_channel(1148273955728281683)
            if channel:
                await channel.send("Ending focus session")
                await end_focus(user="tren_brahh")  
            else:
                print("Channel not found.")
            await asyncio.sleep(60)
            
        if current_time.hour == 17 and current_time.minute == 30: 
            channel = bot.get_channel(1148273955728281683)
            if channel:
                await channel.send("Ending focus session")
                await end_focus(user="tren_brahh")  
            else:
                print("Channel not found.")
            await asyncio.sleep(60)
            
        if current_time.hour == 17 and current_time.minute == 40: 
            channel = bot.get_channel(1148273955728281683)
            if channel:
                await channel.send("Ending focus session")
                await end_focus(user="tren_brahh")  
            else:
                print("Channel not found.")
            await asyncio.sleep(60)
            
        if current_time.hour == 19 and current_time.minute == 00: 
            channel = bot.get_channel(1148273955728281683)
            if channel:
                await channel.send("Ending focus session")
                await end_focus(user="tren_brahh")  
            else:
                print("Channel not found.")
            await asyncio.sleep(60)
            
        if current_time.hour == 21 and current_time.minute == 00: 
            channel = bot.get_channel(1148273955728281683)
            if channel:
                await channel.send("Ending focus session")
                await end_focus(user="tren_brahh")  
            else:
                print("Channel not found.")
            await asyncio.sleep(60)
            
        if current_time.hour >= 21 and current_time.minute >= 46: 
            channel = bot.get_channel(1148273955728281683)
            if channel:
                await channel.send("It's bed time, About to put your PC to sleep. See you in the morning, have a good night 🌙")
                time.sleep(60)
                put_computer_to_sleep()
            else:
                print("Channel not found.")
            await asyncio.sleep(60)
        
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.display_name}')
    bot.loop.create_task(send_dm_when_time_reached()) 

bot.run(BOT_TOKEN)
