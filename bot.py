import os
import discord
from dotenv import load_dotenv
from random import randint

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('anya hug'):
        gif = hug_gif()
        await message.channel.send(file=discord.File(gif))

def hug_gif():
    path = os.path.join("gifs", "hugs")
    gif_list = os.listdir(path)
    gif = gif_list[randint(0, len(gif_list)-1)]
    return os.path.join(path, gif)



client.run(TOKEN)