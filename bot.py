import discord
from discord.ext import commands
import os
from dotenv import find_dotenv, load_dotenv
import torch
import json
from nltk_utils import bag_of_words, tokenize
from model import NeuralNet
from functions.focus import start_focus, end_focus
from functions.spotify_functions import play_song, pause_song, resume_song, skip_track, previous_track, get_current_track
from functions.extract_song_title import extract_song_title

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
BOT_TOKEN = os.getenv('TOKEN')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load intents from intents.json
with open('intents.json', 'r') as json_data:
    intents_data = json.load(json_data)

# Load the trained model and data
FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

# Create a NeuralNet model
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# Create a Discord bot instance
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready(): 
    print(f'We have logged in as {bot.user.display_name}')

@bot.event
async def on_message(message):    
    if message.author == bot.user:
        return
    
    if message.author.name == "Dummy": 
        return

    user_message = message.content
    sentence = tokenize(user_message)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    
    if prob.item() > 0.75:
        for intent in intents_data['intents']:
            if tag == intent["tag"]:
                if tag == "start_focus_session": 
                    await message.channel.send("Sure...Starting a focus session")
                    await start_focus(message.author)
                if tag == "end_focus_session":
                    await message.channel.send("Ending focus session...")
                    await end_focus(message.author)
                    await message.channel.send("unblocked all entertainment websites")
                if tag == "play_song": 
                    normal_text = message.content

                    user_message = normal_text
                    song_title = extract_song_title(user_message)
                    if song_title:
                        await play_song(song=song_title, user=message.author)
                    else:
                        await message.channel.send("No song title found in the message.")
                if tag == "pause_song": 
                    await pause_song(message.author)
                if tag == "resume_song": 
                    await resume_song(message.author)
                if tag == "skip_track": 
                    await skip_track(message.author)
                if tag == "previous_track":
                    await previous_track(message.author)  
                if tag == "get_current_song": 
                    await get_current_track(message.author)      
    else:       
        await message.channel.send("I do not understand...")
        

bot.run(BOT_TOKEN)
