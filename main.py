import os

import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

"""
TODO:
    * Find a way to fetch ELO ratings from aoe4world API
    * Add commands
"""
response = requests.get("https://aoe4world.com/api")
print(f'Connection status code: {response.status_code}')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$',intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord')

@bot.command()
async def elo(ctx):
    await ctx.send("Your ELO is 1180!")

@bot.command()
async def games(ctx, ign: str):
    parameters = {"query": ign}
    user_profile = requests.get("https://aoe4world.com/api/v0/leaderboards/rm_solo", params=parameters)

    games_count = user_profile.json()['players'][0]['games_count']
    wins_count = user_profile.json()['players'][0]['wins_count']
    win_rate = user_profile.json()['players'][0]['win_rate']

    await ctx.send(f"Games record in 1v1 RM for: {ign}\nGames Count: {games_count}\nWins Count: {wins_count}\nWin Rate: {win_rate}")

bot.run(TOKEN)