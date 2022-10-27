import os
from dotenv import load_dotenv

import requests

import discord
from discord.ext import commands

"""
    TODO:
        * Find a way to fetch ELO ratings from aoe4world API
        * Add commands
            * Finish implementing `display top 10 players in rm_solo leaderboards`
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
    '''
    Once the bot has connected to discord, print to output
    that connection is successful
    '''
    print(f'{bot.user} has connected to Discord')

@bot.command()
async def elo(ctx):
    '''
    Useless command until hidden ELO is exposed to aoe4world API 
    '''
    await ctx.send("Your ELO is 1180!")

@bot.command()
async def games(ctx, ign: str):
    '''
    THIS IS UGLY
    '''
    parameters = {"query": ign}
    user_profile = requests.get("https://aoe4world.com/api/v0/leaderboards/rm_solo", params=parameters)

    games_count = user_profile.json()['players'][0]['games_count']
    wins_count = user_profile.json()['players'][0]['wins_count']
    win_rate = user_profile.json()['players'][0]['win_rate']

    await ctx.send(f"Games record in 1v1 RM for: {ign}\nGames Count: {games_count}\nWins Count: {wins_count}\nWin Rate: {win_rate}")

@bot.command()
async def leaderboard(ctx): 
    '''
    INCOMPLETE
    '''
    board = requests.get("https://aoe4world.com/api/v0/leaderboards/rm_solo")

    await ctx.send("Top 10 in 1v1 Ladder")
    for i in range(10):
        await ctx.send(f"{i+1}: {board.json()['players'][i]['name']}")

bot.run(TOKEN)