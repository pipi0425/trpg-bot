# import discord.py
import discord

#import these to get token from .env
import os
from dotenv import load_dotenv

# read .env
load_dotenv()

# load TOKEN from .env
TOKEN = os.getenv("DISCORD_TOKEN")

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

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# end with this line
client.run(TOKEN)