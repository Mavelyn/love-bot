import discord
import redis
from discord.ext import commands

r = redis.Redis()
TOKEN = str(r.get("DISCORD_TOKEN").decode("utf-8"))

client = discord.Client()

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


@bot.command(name="addmovie")
async def add_movie(ctx, *, movie):
    if r.exists("Movies"):
        r.rpush("Movies", movie)
    else:
        r.set("Movies", [movie])
    await ctx.send("New movie added.")


@bot.command(name="movies")
async def movie_list(ctx, movie):
    if r.exists("Movies"):
        movies = r.get("Movies")
        await ctx.send(movies)
    else:
        await ctx.send("No movies found.")


@bot.command(name="adddateidea")
async def add_date_idea(ctx, *, date_idea):
    if r.exists("Date Ideas"):
        r.rpush("Date Ideas", date_idea)
        await ctx.send("New date idea added.")
    else:
        await ctx.send("No date ideas found.")


@bot.command(name="dateideas")
async def date_ideas(ctx):
    if r.exists("Date Ideas"):
        date_ideas = r.get("Date_Ideas")
        await ctx.send(date_ideas)
    else:
        await ctx.send("No date ideas found.")


@bot.command(name="cutestboi")
async def cutie(ctx):
    await ctx.send("Richard Wei uwu")


bot.run(TOKEN)
