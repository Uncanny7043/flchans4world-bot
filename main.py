import discord
import requests
import os
from dotenv import load_dotenv

response = requests.get("https://aoe4world.com/api")
print(f'Connection status code: {response.status_code}')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

client.run(TOKEN)