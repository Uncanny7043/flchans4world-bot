import time

from os import getenv
from dotenv import load_dotenv

import requests

import discord
from discord.ext import commands

"""
    TODO:
        * Find a way to fetch ELO ratings from aoe4world API
        * Add commands
            * Finish implementing `display top 10 players in rm_solo leaderboards`
                * Add more player information
"""

response = requests.get("https://aoe4world.com/api")
print(f'Connection status code: {response.status_code}')

load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')

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

    #await ctx.send(f"Games record in 1v1 RM for: {ign}\nGames Count: {games_count}\nWins Count: {wins_count}\nWin Rate: {win_rate}")

    embed = discord.Embed(title="Match record for:", description=f"{ign}")
    embed.add_field(name="Games Count:", value=games_count, inline=False)
    embed.add_field(name="Wins Count:", value=wins_count, inline=False)
    embed.add_field(name="Win Rate:", value=f"{win_rate}%", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def leaderboard(ctx): 
    '''
    INCOMPLETE: add more player info
    '''
    board = requests.get("https://aoe4world.com/api/v0/leaderboards/rm_solo")

    t = time.strftime("%m/%d/%Y %H:%M")

    embed = discord.Embed(title="Top 10 in 1v1 Ladder", description=f"`as of {t}`")
    for i in range(10):
        embed.add_field(name=f"{i+1}. {board.json()['players'][i]['name']}", value="placeholder", inline=False)
    
    await ctx.send(embed=embed)
    
@bot.command()
async def test(ctx):
    embed = discord.Embed(title="Fuck you", description="Ottoids suck") #,color=Hex code
    embed.add_field(name="Name", value="you can make as much as fields you like to")
    embed.set_footer(text="footer") #if you like to
    await ctx.send(embed=embed)

bot.run(TOKEN)