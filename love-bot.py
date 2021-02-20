import os
import discord
import redis
from dotenv import load_dotenv
from discord.ext import commands

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')

redis_server = redis.Redis()
TOKEN = str(redis_server.get('DISCORD_TOKEN').decode('utf-8'))

client = discord.Client()

bot = commands.Bot(command_prefix='!')

movies = []
date_ideas = []
restaurants = []


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name="movies")
async def movie_list(ctx, movie):
    movies.append(movie)
    await ctx.send(movies)


@bot.command(name="dateideas")
async def date_ideas(ctx):
    await ctx.send(date_ideas)


@bot.command(name="restaurants")
async def restaurant_list(ctx):
    await ctx.send(restaurants)


@bot.command(name="cutestboi")
async def cutie(ctx):
    await ctx.send("Richard Wei uwu")


bot.run(TOKEN)
