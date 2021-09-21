# import discord.py
import discord

#import these to get token from .env
import os
from dotenv import load_dotenv

# read .env
load_dotenv()

# load variables from .env
TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("PREFIX")

# start discord client for the bot
client = discord.Client()

# on_ready
@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

# on_message
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    #check prefix or mentioned
    if message.content.startswith(PREFIX) or client.user in message.mentions:
        await message.channel.send('hello')
    

# end with this line
client.run(TOKEN)