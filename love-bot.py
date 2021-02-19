import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix='!')

movies = []
date_ideas = []


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    

@bot.command(name="movies")
async def movie_list(ctx, movie):
    movies.append(movie)
    await ctx.send(movies)


bot.run(TOKEN)
