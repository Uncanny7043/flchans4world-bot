import discord
import requests

response = requests.get("https://aoe4world.com/api")
print(response.status_code)

TOKEN = 'MTAzNDY2NzY5ODAwNjgwMjQ1Mw.GjbHN-.-a6i8MsDQJykLCZPRMgUL7ApgyV7ruKWv8qED8'

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

client.run(TOKEN)