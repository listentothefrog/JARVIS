import discord
from discord.ext import commands
import os
from dotenv import find_dotenv, load_dotenv
import torch
import json
from nltk_utils import bag_of_words, tokenize
from model import NeuralNet

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


bot.run(BOT_TOKEN)
